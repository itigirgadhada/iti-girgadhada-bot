import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# TOKEN ને Environment Variable માંથી લો
TOKEN = os.getenv("TOKEN")  # Render પર TOKEN ઉમેરાશે

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📚 ટ્રેડ્સની માહિતી", callback_data='trades')],
        [InlineKeyboardButton("✅ એલિજિબિલિટી", callback_data='eligibility')],
        [InlineKeyboardButton("📝 ડોક્યુમેન્ટ્સ", callback_data='documents')],
        [InlineKeyboardButton("💵 ફી", callback_data='fees')],
        [InlineKeyboardButton("📋 એડમિશન પ્રોસેસ", callback_data='process')],
        [InlineKeyboardButton("🎁 સંસ્થા તરફથી મળતી સુવિધા", callback_data='facilities')],
        [InlineKeyboardButton("📄 એડમિશન PDF ડાઉનલોડ", callback_data='download_pdf')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "નમસ્તે! ઔદ્યોગિક તાલીમ સંસ્થા ગીરગઢડા (ITI Girgadhada) ના 2025 એડમિશન વિશે માહિતી મેળવવા માટે આપનું સ્વાગત છે! 🙏\n"
        "કૃપા કરી નીચેના ઓપ્શન્સમાંથી એક પસંદ કરો:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'trades':
        keyboard = [
            [InlineKeyboardButton("COPA", callback_data='trade_copa')],
            [InlineKeyboardButton("ઇલેક્ટ્રિશિયન", callback_data='trade_electrician')],
            [InlineKeyboardButton("ફીટર", callback_data='trade_fitter')],
            [InlineKeyboardButton("વેલ્ડર", callback_data='trade_welder')],
            [InlineKeyboardButton("મિકેનિક ડીઝલ", callback_data='trade_mechanic_diesel')],
            [InlineKeyboardButton("હેલ્થ સેનેટરી ઇન્સ્પેક્ટર", callback_data='trade_health_sanitary_inspector')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(
            "કૃપા કરી નીચેના ટ્રેડ્સમાંથી એક પસંદ કરો:",
            reply_markup=reply_markup
        )
    elif query.data == 'trade_copa':
        await query.message.reply_text(
            "📚 **COPA (કમ્પ્યુટર ઓપરેટર એન્ડ પ્રોગ્રામિંગ આસિસ્ટન્ટ)**\n"
            "- સમયગાળો: 1 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 72"
        )
    elif query.data == 'trade_electrician':
        await query.message.reply_text(
            "📚 **ઇલેક્ટ્રિશિયન**\n"
            "- સમયગાળો: 2 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 60"
        )
    elif query.data == 'trade_fitter':
        await query.message.reply_text(
            "📚 **ફીટર**\n"
            "- સમયગાળો: 2 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 40"
        )
    elif query.data == 'trade_welder':
        await query.message.reply_text(
            "📚 **વેલ્ડર**\n"
            "- સમયગાળો: 1 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 40"
        )
    elif query.data == 'trade_mechanic_diesel':
        await query.message.reply_text(
            "📚 **મિકેનિક ડીઝલ**\n"
            "- સમયગાળો: 1 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 72"
        )
    elif query.data == 'trade_health_sanitary_inspector':
        await query.message.reply_text(
            "📚 **હેલ્થ સેનેટરી ઇન્સ્પેક્ટર**\n"
            "- સમયગાળો: 1 વર્ષ\n"
            "- ઉપલબ્ધ બેઠકો: 72"
        )
    elif query.data == 'eligibility':
        await query.message.reply_text(
            "એલિજિબિલિટી:\n- વેલ્ડર ટ્રેડ: ધોરણ 8 પાસ\n- અન્ય ટ્રેડ્સ (COPA, ઇલેક્ટ્રિશિયન, ફીટર, મિકેનિક ડીઝલ, હેલ્થ સેનેટરી ઇન્સ્પેક્ટર): ધોરણ 10 પાસ"
        )
    elif query.data == 'documents':
        await query.message.reply_text(
            "એડમિશન માટે જરૂરી ડોક્યુમેન્ટ્સ:\n1. લિવિંગ સર્ટિફિકેટ\n2. માર્કશીટ\n3. જાતિનો દાખલો\n4. આધાર કાર્ડ"
        )
    elif query.data == 'fees':
        await query.message.reply_text(
            "ફોર્મ ભરવાની ફી: ₹50 (ઓનલાઈન)"
        )
    elif query.data == 'process':
        await query.message.reply_text(
            "એડમિશન પ્રોસેસ:\n1. ઓનલાઈન ફોર્મ ભરો\n2. જરૂરી ડોક્યુમેન્ટ્સ અપલોડ કરો\n3. ₹50 ફી ઓનલાઈન ચૂકવો\n4. ફોર્મ સબમિટ કરો"
        )
    elif query.data == 'facilities':
        await query.message.reply_text(
            "🎁 **સંસ્થા તરફથી મળતી સુવિધા**:\n"
            "1. વિના મૂલ્યે બસ પાસ\n"
            "2. ₹4800/- શિષ્યવૃત્તિ\n"
            "3. મહિલા તાલીમાર્થીઓને સાયકલ સહાય\n"
            "4. ધોરણ 12 સમકક્ષતાનો લાભ"
        )
    elif query.data == 'download_pdf':
        await query.message.reply_text(
            "📄 **એડમિશન PDF ડાઉનલોડ**:\n"
            "એડમિશન સંબંધિત વિગતો માટે PDF ફાઈલ ડાઉનલોડ કરો:\n"
            "[ડાઉનલોડ કરો](https://github.com/your-username/iti-girgadhada-bot/raw/main/admission_info.pdf)"
        )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()
