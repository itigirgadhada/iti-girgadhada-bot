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
        [InlineKeyboardButton("📋 એડમિશન પ્રોસેસ", callback_data='process')]
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
        await query.message.reply_text(
            "ITI ગીરગઢડામાં નીચેના ટ્રેડ્સ ઉપલબ્ધ છે:\n"
            "1. COPA (1 વર્ષ)\n2. ઇલેક્ટ્રિશિયન (2 વર્ષ)\n3. ફીટર (2 વર્ષ)\n"
            "4. વેલ્ડર (1 વર્ષ)\n5. મિકેનિક ડીઝલ (1 વર્ષ)\n6. હેલ્થ સેનેટરી ઇન્સ્પેક્ટર (1 વર્ષ)"
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

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()
