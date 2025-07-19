# bot.py (উদাহরণ)

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import *
from script import Script

# বট ক্লায়েন্ট তৈরি
app = Client(
    SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# --- অটো-ডিলিট কাউন্টডাউন ফাংশন ---
async def auto_delete_message_with_countdown(message: Message, time: int):
    """Deletes a message after a countdown, editing it periodically."""
    try:
        # মেসেজের মূল টেক্সট সেভ করে রাখা
        original_text = message.text or message.caption
        if not original_text:
            original_text = ""

        # কাউন্টডাউন লুপ
        for i in range(time, 0, -10): # প্রতি ১০ সেকেন্ডে আপডেট হবে
            remaining_time = max(i - 10, 0)
            countdown_text = f"\n\n**⚠️ This message will be deleted in `{remaining_time}` seconds.**"
            try:
                await message.edit_text(original_text + countdown_text)
            except Exception:
                pass # যদি মেসেজ এডিট করা না যায়
            await asyncio.sleep(10)
        
        # ডিলিট করা
        await message.delete()
    except Exception as e:
        print(f"Error in auto-delete: {e}")

# --- স্টার্ট কমান্ড হ্যান্ডলার ---
@app.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    user_first_name = message.from_user.first_name
    
    # ইনলাইন বাটন
    buttons = [
        [InlineKeyboardButton("➕ Add Me To Your Group ➕", url=f"http://t.me/Surya_X_Provider_Subot?startgroup=true")],
        [
            InlineKeyboardButton("💬 Help", callback_data="help"),
            InlineKeyboardButton("🤖 About", callback_data="about")
        ],
        [InlineKeyboardButton("❤️ Owner", url="https://t.me/Mr_SuryaBhaskar")]
    ]
    
    await message.reply_text(
        text=Script.START_TEXT.format(user_first_name=user_first_name),
        reply_markup=InlineKeyboardMarkup(buttons),
        disable_web_page_preview=True
    )

# --- ফিল্টার হ্যান্ডলার (গ্রুপ ও চ্যানেলে কাজ করবে) ---
@app.on_message(filters.text & (filters.group | filters.channel))
async def auto_filter_handler(client: Client, message: Message):
    # এখানে আপনার মুভি খোঁজার এবং ফাইল পাঠানোর লজিক থাকবে
    # যেমন ডেটাবেস থেকে ফাইল খুঁজে বের করা
    
    # --- উদাহরণ: ফাইল পাঠানোর পর অটো-ডিলিট কল করা ---
    # sent_message = await message.reply_text("Here is your file!") # ফাইল পাঠানোর পর
    
    # if AUTO_DELETE:
    #     asyncio.create_task(auto_delete_message_with_countdown(sent_message, DELETE_TIME))
    pass


# --- ফাইল পাঠানোর উদাহরণ (এই অংশটি আপনার নিজের লজিক অনুযায়ী পরিবর্তন করুন) ---
async def send_file_to_user(user_id, file_info):
    # শর্টনার ছাড়াই সরাসরি লিঙ্ক দেওয়া হবে
    file_caption = Script.FILE_CAPTION.format(
        title=file_info.get('title', 'N/A'),
        quality=file_info.get('quality', 'N/A'),
        audio=file_info.get('audio', 'N/A'),
        language=file_info.get('language', 'N/A'),
        size=file_info.get('size', 'N/A')
    )
    
    sent_message = await app.send_document(
        chat_id=user_id,
        document=file_info['file_id'],
        caption=file_caption
    )
    
    # অটো-ডিলিট ফাংশন কল করা
    if AUTO_DELETE:
        asyncio.create_task(auto_delete_message_with_countdown(sent_message, DELETE_TIME))
        

# বট চালানো
if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
