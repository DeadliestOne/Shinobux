import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions
from ANNIEMUSIC import app 

spam_chats = []


GM_MESSAGES = [ "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴋᴇsᴇ ʜᴏ 🐱**",
         "**➠ ɢᴍ, sᴜʙʜᴀ ʜᴏ ɢʏɪ ᴜᴛʜɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 🌤️**",
         "**➠ ɢᴍ ʙᴀʙʏ, ᴄʜᴀɪ ᴘɪ ʟᴏ ☕**",
         "**➠ ᴊᴀʟᴅɪ ᴜᴛʜᴏ, sᴄʜᴏᴏʟ ɴᴀʜɪ ᴊᴀɴᴀ ᴋʏᴀ 🏫**",
         "**➠ ɢᴍ, ᴄʜᴜᴘ ᴄʜᴀᴘ ʙɪsᴛᴇʀ sᴇ ᴜᴛʜᴏ ᴠʀɴᴀ ᴘᴀɴɪ ᴅᴀʟ ᴅᴜɴɢɪ 🧊**",
         "**➠ ʙᴀʙʏ ᴜᴛʜᴏ ᴀᴜʀ ᴊᴀʟᴅɪ ғʀᴇsʜ ʜᴏ ᴊᴀᴏ, ɴᴀsᴛᴀ ʀᴇᴀᴅʏ ʜᴀɪ 🫕**",
         "**➠ ᴏғғɪᴄᴇ ɴᴀʜɪ ᴊᴀɴᴀ ᴋʏᴀ ᴊɪ ᴀᴀᴊ, ᴀʙʜɪ ᴛᴀᴋ ᴜᴛʜᴇ ɴᴀʜɪ 🏣**",
         "**➠ ɢᴍ ᴅᴏsᴛ, ᴄᴏғғᴇᴇ/ᴛᴇᴀ ᴋʏᴀ ʟᴏɢᴇ ☕🍵**",
         "**➠ ʙᴀʙʏ 8 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ, ᴀᴜʀ ᴛᴜᴍ ᴀʙʜɪ ᴛᴋ ᴜᴛʜᴇ ɴᴀʜɪ 🕖**",
         "**➠ ᴋʜᴜᴍʙʜᴋᴀʀᴀɴ ᴋɪ ᴀᴜʟᴀᴅ ᴜᴛʜ ᴊᴀᴀ... ☃️**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ... 🌄**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʜᴀᴠᴇ ᴀ ɢᴏᴏᴅ ᴅᴀʏ... 🪴**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ʙᴀʙʏ 😇**",
         "**➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ ʏᴇ ɴᴀʟᴀʏᴋ ᴀʙʜɪ ᴛᴀᴋ sᴏ ʀʜᴀ ʜᴀɪ... 😵‍💫**",
         "**➠ ʀᴀᴀᴛ ʙʜᴀʀ ʙᴀʙᴜ sᴏɴᴀ ᴋʀ ʀʜᴇ ᴛʜᴇ ᴋʏᴀ, ᴊᴏ ᴀʙʜɪ ᴛᴋ sᴏ ʀʜᴇ ʜᴏ ᴜᴛʜɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ... 😏**",
         "**➠ ʙᴀʙᴜ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴜᴛʜ ᴊᴀᴏ ᴀᴜʀ ɢʀᴏᴜᴘ ᴍᴇ sᴀʙ ғʀɪᴇɴᴅs ᴋᴏ ɢᴍ ᴡɪsʜ ᴋʀᴏ... 🌟**",
         "**➠ ᴘᴀᴘᴀ ʏᴇ ᴀʙʜɪ ᴛᴀᴋ ᴜᴛʜ ɴᴀʜɪ, sᴄʜᴏᴏʟ ᴋᴀ ᴛɪᴍᴇ ɴɪᴋᴀʟᴛᴀ ᴊᴀ ʀʜᴀ ʜᴀɪ... 🥲**",
         "**➠ ᴊᴀɴᴇᴍᴀɴ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ᴋʏᴀ ᴋʀ ʀʜᴇ ʜᴏ ... 😅**",
         "**➠ ɢᴍ ʙᴇᴀsᴛɪᴇ, ʙʀᴇᴀᴋғᴀsᴛ ʜᴜᴀ ᴋʏᴀ... 🍳**",
        ]


GN_MESSAGES = [ " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌚** ",
           " **➠ ᴄʜᴜᴘ ᴄʜᴀᴘ sᴏ ᴊᴀ 🙊** ",
           " **➠ ᴘʜᴏɴᴇ ʀᴀᴋʜ ᴋᴀʀ sᴏ ᴊᴀ, ɴᴀʜɪ ᴛᴏ ʙʜᴏᴏᴛ ᴀᴀ ᴊᴀʏᴇɢᴀ..👻** ",
           " **➠ ᴀᴡᴇᴇ ʙᴀʙᴜ sᴏɴᴀ ᴅɪɴ ᴍᴇɪɴ ᴋᴀʀ ʟᴇɴᴀ ᴀʙʜɪ sᴏ ᴊᴀᴏ..?? 🥲** ",
           " **➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ ʏᴇ ᴀᴘɴᴇ ɢғ sᴇ ʙᴀᴀᴛ ᴋʀ ʀʜᴀ ʜ ʀᴀᴊᴀɪ ᴍᴇ ɢʜᴜs ᴋᴀʀ, sᴏ ɴᴀʜɪ ʀᴀʜᴀ 😜** ",
           " **➠ ᴘᴀᴘᴀ ʏᴇ ᴅᴇᴋʜᴏ ᴀᴘɴᴇ ʙᴇᴛᴇ ᴋᴏ ʀᴀᴀᴛ ʙʜᴀʀ ᴘʜᴏɴᴇ ᴄʜᴀʟᴀ ʀʜᴀ ʜᴀɪ 🤭** ",
           " **➠ ᴊᴀɴᴜ ᴀᴀᴊ ʀᴀᴀᴛ ᴋᴀ sᴄᴇɴᴇ ʙɴᴀ ʟᴇ..?? 🌠** ",
           " **➠ ɢɴ sᴅ ᴛᴄ.. 🙂** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ ᴛᴀᴋᴇ ᴄᴀʀᴇ..?? ✨** ",
           " **➠ ʀᴀᴀᴛ ʙʜᴜᴛ ʜᴏ ɢʏɪ ʜᴀɪ sᴏ ᴊᴀᴏ, ɢɴ..?? 🌌** ",
           " **➠ ᴍᴜᴍᴍʏ ᴅᴇᴋʜᴏ 11 ʙᴀᴊɴᴇ ᴡᴀʟᴇ ʜᴀɪ ʏᴇ ᴀʙʜɪ ᴛᴀᴋ ᴘʜᴏɴᴇ ᴄʜᴀʟᴀ ʀʜᴀ ɴᴀʜɪ sᴏ ɴᴀʜɪ ʀʜᴀ 🕦** ",
           " **➠ ᴋᴀʟ sᴜʙʜᴀ sᴄʜᴏᴏʟ ɴᴀʜɪ ᴊᴀɴᴀ ᴋʏᴀ, ᴊᴏ ᴀʙʜɪ ᴛᴀᴋ ᴊᴀɢ ʀʜᴇ ʜᴏ 🏫** ",
           " **➠ ʙᴀʙᴜ, ɢᴏᴏᴅ ɴɪɢʜᴛ sᴅ ᴛᴄ..?? 😊** ",
           " **➠ ᴀᴀᴊ ʙʜᴜᴛ ᴛʜᴀɴᴅ ʜᴀɪ, ᴀᴀʀᴀᴍ sᴇ ᴊᴀʟᴅɪ sᴏ ᴊᴀᴛɪ ʜᴏᴏɴ 🌼** ",
           " **➠ ᴊᴀɴᴇᴍᴀɴ, ɢᴏᴏᴅ ɴɪɢʜᴛ 🌷** ",
           " **➠ ᴍᴇ ᴊᴀ ʀᴀʜɪ sᴏɴᴇ, ɢɴ sᴅ ᴛᴄ 🏵️** ",
           " **➠ ʜᴇʟʟᴏ ᴊɪ ɴᴀᴍᴀsᴛᴇ, ɢᴏᴏᴅ ɴɪɢʜᴛ 🍃** ",
           " **➠ ʜᴇʏ, ʙᴀʙʏ ᴋᴋʀʜ..? sᴏɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ ☃️** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ, ʙʜᴜᴛ ʀᴀᴀᴛ ʜᴏ ɢʏɪ..? ⛄** ",
           " **➠ ᴍᴇ ᴊᴀ ʀᴀʜɪ ʀᴏɴᴇ, ɪ ᴍᴇᴀɴ sᴏɴᴇ ɢᴏᴏᴅ ɴɪɢʜᴛ ᴊɪ 😁** ",
           " **➠ ᴍᴀᴄʜʜᴀʟɪ ᴋᴏ ᴋᴇʜᴛᴇ ʜᴀɪ ғɪsʜ, ɢᴏᴏᴅ ɴɪɢʜᴛ ᴅᴇᴀʀ ᴍᴀᴛ ᴋʀɴᴀ ᴍɪss, ᴊᴀ ʀʜɪ sᴏɴᴇ 🌄** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ ʙʀɪɢʜᴛғᴜʟʟ ɴɪɢʜᴛ 🤭** ",
           " **➠ ᴛʜᴇ ɴɪɢʜᴛ ʜᴀs ғᴀʟʟᴇɴ, ᴛʜᴇ ᴅᴀʏ ɪs ᴅᴏɴᴇ,, ᴛʜᴇ ᴍᴏᴏɴ ʜᴀs ᴛᴀᴋᴇɴ ᴛʜᴇ ᴘʟᴀᴄᴇ ᴏғ ᴛʜᴇ sᴜɴ... 😊** ",
           " **➠ ᴍᴀʏ ᴀʟʟ ʏᴏᴜʀ ᴅʀᴇᴀᴍs ᴄᴏᴍᴇ ᴛʀᴜᴇ ❤️** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴘʀɪɴᴋʟᴇs sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ 💚** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ, ɴɪɴᴅ ᴀᴀ ʀʜɪ ʜᴀɪ 🥱** ",
           " **➠ ᴅᴇᴀʀ ғʀɪᴇɴᴅ ɢᴏᴏᴅ ɴɪɢʜᴛ 💤** ",
           " **➠ ʙᴀʙʏ ᴀᴀᴊ ʀᴀᴀᴛ ᴋᴀ sᴄᴇɴᴇ ʙɴᴀ ʟᴇ 🥰** ",
           " **➠ ɪᴛɴɪ ʀᴀᴀᴛ ᴍᴇ ᴊᴀɢ ᴋᴀʀ ᴋʏᴀ ᴋᴀʀ ʀʜᴇ ʜᴏ sᴏɴᴀ ɴᴀʜɪ ʜᴀɪ ᴋʏᴀ 😜** ",
           " **➠ ᴄʟᴏsᴇ ʏᴏᴜʀ ᴇʏᴇs sɴᴜɢɢʟᴇ ᴜᴘ ᴛɪɢʜᴛ,, ᴀɴᴅ ʀᴇᴍᴇᴍʙᴇʀ ᴛʜᴀᴛ ᴀɴɢᴇʟs, ᴡɪʟʟ ᴡᴀᴛᴄʜ ᴏᴠᴇʀ ʏᴏᴜ ᴛᴏɴɪɢʜᴛ... 💫** ",
           ]

HI_MESSAGES = [ " **❅ बेबी कहा हो। 🤗** ",
           " **❅ ओए सो गए क्या, ऑनलाइन आओ ।😊** ",
           " **❅ ओए वीसी आओ बात करते हैं । 😃** ",
           " **❅ खाना खाया कि नही। 🥲** ",
           " **❅ घर में सब कैसे हैं। 🥺** ",
           " **❅ पता है बहुत याद आ रही आपकी। 🤭** ",
           " **❅ और बताओ कैसे हो।..?? 🤨** ",
           " **❅ मेरी भी सैटिंग करवा दो प्लीज..?? 🙂** ",
           " **❅ आपका नाम क्या है।..?? 🥲** ",
           " **❅ नाश्ता हो गया..?? 😋** ",
           " **❅ मुझे अपने ग्रूप में ऐड कर लो। 😍** ",
           " **❅ आपका दोस्त आपको बुला रहा है। 😅** ",
           " **❅ मुझसे शादी करोगे ..?? 🤔** ",
           " **❅ सोने चले गए क्या 🙄** ",
           " **❅ अरे यार कोई AC चला दो 😕** ",
           " **❅ आप कहा से हो..?? 🙃** ",
           " **❅ हेलो जी नमस्ते 😛** ",
           " **❅ BABY क्या कर रही हो..? 🤔** ",
           " **❅ क्या आप मुझे जानते हो .? ☺️** ",
           " **❅ आओ baby Ludo खेलते है .🤗** ",
           " **❅ चलती है क्या 9 से 12... 😇** ",
           " **❅ आपके पापा क्या करते है 🤭** ",
           " **❅ आओ baby बाजार चलते है गोलगप्पे खाने। 🥺** ",
           " **❅ अकेली ना बाजार जाया करो, नज़र लग जायेगी। 😶** ",
           " **❅ और बताओ BF कैसा है ..?? 🤔** ",
           " **❅ गुड मॉर्निंग 😜** ",
           " **❅ मेरा एक काम करोगे। 🙂** ",
           " **❅ DJ वाले बाबू मेरा गाना चला दो। 😪** ",
           " **❅ आप से मिलकर अच्छा लगा।☺** ",
           " **❅ मेरे बाबू ने थाना थाया।..? 🙊** ",
           " **❅ पढ़ाई कैसी चल रही हैं ? 😺** ",
           " **❅ हम को प्यार हुआ। 🥲** ",
           " **❅ Nykaa कौन है...? 😅** ",
           " **❅ तू खींच मेरी फ़ोटो ..? 😅** ",
           " **❅ Phone काट मम्मी आ गई क्या। 😆** ",
           " **❅ और भाबी से कब मिल वा रहे हो । 😉** ",
           " **❅ क्या आप मुझसे प्यार करते हो 💚** ",
           " **❅ मैं तुम से बहुत प्यार करती हूं..? 👀** ",
           " **❅ बेबी एक kiss दो ना..?? 🙉** ",
           " **❅ एक जॉक सुनाऊं..? 😹** ",
           " **❅ vc पर आओ कुछ दिखाती हूं  😻** ",
           " **❅ क्या तुम instagram चलते हो..?? 🙃** ",
           " **❅ whatsapp नंबर दो ना अपना..? 😕** ",
           " **❅ आप की दोस्त से मेरी सेटिंग करा दो ..? 🙃** ",
           " **❅ सारा काम हो गया हो तो ऑनलाइन आ जाओ।..? 🙃** ",
           " **❅ कहा से हो आप 😊** ",
           " **❅ जा तुझे आज़ाद कर दिया मैंने मेरे दिल से। 🥺** ",
           " **❅ मेरा एक काम करोगे, ग्रूप मे कुछ मेंबर ऐड कर दो ..? ♥️** ",
           " **❅ मैं तुमसे नाराज़ हूं 😠** ",
           " **❅ आपकी फैमिली कैसी है..? ❤** ",
           " **❅ क्या हुआ..? 🤔** ",
           " **❅ बहुत याद आ रही है आपकी 😒** ",
           " **❅ भूल गए मुझे 😏** ",
           " **❅ झूठ क्यों बोला आपने मुझसे 🤐** ",
           " **❅ इतना भाव मत खाया करो, रोटी खाया करो कम से कम मोटी तो हो जाओगी 😒** ",
           " **❅ ये attitude किसे दिखा रहे हो 😮** ",
           " **❅ हेमलो कहा busy ho 👀** ",
           " **❅ आपके जैसा दोस्त पाकर मे बहुत खुश हूं। 🙈** ",
           " **❅ आज मन बहुत उदास है ☹️** ",
           " **❅ मुझसे भी बात कर लो ना 🥺** ",
           " **❅ आज खाने में क्या बनाया है 👀** ",
           " **❅ क्या चल रहा है 🙂** ",
           " **❅ message क्यों नहीं करती हो..🥺** ",
           " **❅ मैं मासूम हूं ना 🥺** ",
           " **❅ कल मज़ा आया था ना 😅** ",
           " **❅ कल कहा busy थे 😕** ",
           " **❅ आप relationship में हो क्या..? 👀** ",
           " **❅ कितने शांत रहते हो यार आप 😼** ",
           " **❅ आपको गाना, गाना आता है..? 😸** ",
           " **❅ घूमने चलोगे मेरे साथ..?? 🙈** ",
           " **❅ हमेशा हैप्पी रहा करो यार 🤞** ",
           " **❅ क्या हम दोस्त बन सकते है...? 🥰** ",
           " **❅ आप का विवाह हो गया क्या.. 🥺** ",
           " **❅ कहा busy the इतने दिनों से 🥲** ",
           " **❅ single हो या mingle 😉** ",
           " **❅ आओ पार्टी करते है 🥳** ",
           " **❅ Bio में link हैं join कर लो 🧐** ",
           " **❅ मैं तुमसे प्यार नहीं करती, 🥺** ",
           " **❅ यहां आ जाओ ना @TEAM_CDX मस्ती करेंगे 🤭** ",
           " **❅ भूल जाओ मुझे,..? 😊** ",
           " **❅ अपना बना ले पिया, अपना बना ले 🥺** ",
           " **❅ मेरा ग्रुप भी join कर लो ना 🤗** ",
           " **❅ मैने तेरा नाम Dil rakh diya 😗** ",
           " **❅ तुमारे सारे दोस्त कहा गए 🥺** ",
           " **❅ 𝐈𝐬𝐦𝐞 𝐚𝐚 𝐣𝐚𝐨 𝐟𝐥𝐢𝐫𝐭 𝐤𝐫𝐞𝐧𝐠𝐞 @BWANDARLOK 🥰** ",
           " **❅ किसकी याद मे खोए हो जान 😜** ",
           " **❅ गुड नाईट जी बहुत रात हो गई 🥰** ",
           ]

QUOTES = [ "**❅ ɪғ ʏᴏᴜ ᴅᴏ ɴᴏᴛ sᴛᴇᴘ ғᴏʀᴡᴀʀᴅ ʏᴏᴜ ᴡɪʟʟ ʀᴇᴍᴀɪɴ ɪɴ ᴛʜᴇ sᴀᴍᴇ ᴘʟᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ʜᴀʀᴅ ʙᴜᴛ ɴᴏᴛ ɪᴍᴘᴏssɪʙʟᴇ.**",
         "**❅ ʟɪғᴇ’s ᴛᴏᴏ sʜᴏʀᴛ ᴛᴏ ᴀʀɢᴜᴇ ᴀɴᴅ ғɪɢʜᴛ.**",
         "**❅ ᴅᴏɴ’ᴛ ᴡᴀɪᴛ ғᴏʀ ᴛʜᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛ ᴛᴀᴋᴇ ᴍᴏᴍᴇɴᴛ ᴀɴᴅ ᴍᴀᴋᴇ ɪᴛ ᴘᴇʀғᴇᴄᴛ.**",
         "**❅ sɪʟᴇɴᴄᴇ ɪs ᴛʜᴇ ʙᴇsᴛ ᴀɴsᴡᴇʀ ᴛᴏ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ᴅᴏᴇsɴ’ᴛ ᴠᴀʟᴜᴇ ʏᴏᴜʀ ᴡᴏʀᴅs.**",
         "**❅ ᴇᴠᴇʀʏ ɴᴇᴡ ᴅᴀʏ ɪs ᴀ ᴄʜᴀɴᴄᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ, ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ᴘʀɪᴏʀɪᴛɪᴇs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴊᴏᴜʀɴᴇʏ, ɴᴏᴛ ᴀ ʀᴀᴄᴇ..**",
         "**❅ sᴍɪʟᴇ ᴀɴᴅ ᴅᴏɴ’ᴛ ᴡᴏʀʀʏ, ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ.**",
         "**❅ ᴅᴏ ɴᴏᴛ ᴄᴏᴍᴘᴀʀᴇ ʏᴏᴜʀsᴇʟғ ᴛᴏ ᴏᴛʜᴇʀs ɪғ ʏᴏᴜ ᴅᴏ sᴏ ʏᴏᴜ ᴀʀᴇ ɪɴsᴜʟᴛɪɴɢ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ ɪ ᴀᴍ ɪɴ ᴛʜᴇ ᴘʀᴏᴄᴇss ᴏғ ʙᴇᴄᴏᴍɪɴɢ ᴛʜᴇ ʙᴇsᴛ ᴠᴇʀsɪᴏɴ ᴏғ ᴍʏsᴇʟғ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ɪᴄᴇ ᴇɴᴊᴏʏ ɪᴛ ʙᴇғᴏʀᴇ ɪᴛ ᴍᴇʟᴛs.**",
         "**❅ ʙᴇ ғʀᴇᴇ ʟɪᴋᴇ ᴀ ʙɪʀᴅ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴀᴛ ᴛʜᴇ ᴇɴᴅ ᴏғ ʏᴏᴜʀ ᴄᴏᴍғᴏʀᴛ ᴢᴏɴᴇ.**",
         "**❅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢs ᴛʜᴀᴛ ʜᴜʀᴛ ʏᴏᴜ, ᴀᴄᴛᴜᴀʟʟʏ ᴛᴇᴀᴄʜ ʏᴏᴜ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴄᴀᴍᴇʀᴀ. sᴏ ғᴀᴄᴇ ɪᴛ ᴡɪᴛʜ ᴀ sᴍɪʟᴇ.**",
         "**❅ ʟɪғᴇ ɪs 10% ᴏғ ᴡʜᴀᴛ ʜᴀᴘᴘᴇɴs ᴛᴏ ʏᴏᴜ ᴀɴᴅ 90% ᴏғ ʜᴏᴡ ʏᴏᴜ ʀᴇsᴘᴏɴᴅ ᴛᴏ ɪᴛ.**",
         "**❅ ʟɪғᴇ ᴀʟᴡᴀʏs ᴏғғᴇʀs ʏᴏᴜ ᴀ sᴇᴄᴏɴᴅ ᴄʜᴀɴᴄᴇ. ɪᴛ’s ᴄᴀʟʟᴇᴅ ᴛᴏᴍᴏʀʀᴏᴡ.**",
         "**❅ ɴᴏ ᴏɴᴇ ɪs ᴄᴏᴍɪɴɢ ᴛᴏ sᴀᴠᴇ ʏᴏᴜ. ᴛʜɪs ʟɪғᴇ ᴏғ ʏᴏᴜʀ ɪs 100% ʏᴏᴜʀ ʀᴇsᴘᴏɴsɪʙɪʟɪᴛʏ..**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀɴ ᴇᴀsʏ ᴛᴀsᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ᴀᴅᴠᴇɴᴛᴜʀᴇ.**",
         "**❅ ʟɪғᴇ ʙᴇɢɪɴs ᴏɴ ᴛʜᴇ ᴏᴛʜᴇʀ sɪᴅᴇ ᴏғ ᴅᴇsᴘᴀɪʀ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴀ ᴘʀᴏʙʟᴇᴍ ᴛᴏ ʙᴇ sᴏʟᴠᴇᴅ ʙᴜᴛ ᴀ ʀᴇᴀʟɪᴛʏ ᴛᴏ ʙᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇᴅ.**",
         "**❅ ʟɪғᴇ ᴅᴏᴇs ɴᴏᴛ ʜᴀᴠᴇ ᴀ ʀᴇᴍᴏᴛᴇ; ɢᴇᴛ ᴜᴘ ᴀɴᴅ ᴄʜᴀɴɢᴇ ɪᴛ ʏᴏᴜʀsᴇʟғ.**",
         "**❅ sᴛᴀʀᴛ ᴛʀᴜsᴛɪɴɢ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʏᴏᴜ’ʟʟ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ʟɪᴠᴇ.**",
         "**❅ ʜᴇᴀʟᴛʜ ɪs ᴛʜᴇ ᴍᴏsᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ɢᴏᴏᴅ ᴏғ ʟɪғᴇ.**",
         "**❅ ᴛɪᴍᴇ ᴄʜᴀɴɢᴇ ᴘʀɪᴏʀɪᴛʏ ᴄʜᴀɴɢᴇs.**",
         "**❅ ᴛᴏ sᴇᴇ ᴀɴᴅ ᴛᴏ ғᴇᴇʟ ᴍᴇᴀɴs ᴛᴏ ʙᴇ, ᴛʜɪɴᴋ ᴀɴᴅ ʟɪᴠᴇ.**",
         "**❅ ʙᴇ ᴡɪᴛʜ sᴏᴍᴇᴏɴᴇ ᴡʜᴏ ʙʀɪɴɢs ᴏᴜᴛ ᴛʜᴇ ʙᴇsᴛ ᴏғ ʏᴏᴜ.**",
         "**❅ ʏᴏᴜʀ ᴛʜᴏᴜɢʜᴛs ᴀʀᴇ ʏᴏᴜʀ ʟɪғᴇ.**",
         "**❅ ᴘᴇᴏᴘʟᴇ ᴄʜᴀɴɢᴇ, ᴍᴇᴍᴏʀɪᴇs ᴅᴏɴ’ᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴡᴇ ᴛʜɪɴᴋ ɪᴛ ɪs.**",
         "**❅ ʟɪɢʜᴛ ʜᴇᴀʀᴛ ʟɪᴠᴇs ʟᴏɴɢᴇʀ.**",
         "**❅ ᴅᴇᴘʀᴇssɪᴏɴ ᴇᴠᴇɴᴛᴜᴀʟʟʏ ʙᴇᴄᴏᴍᴇs ᴀ ʜᴀʙɪᴛ.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ɢɪғᴛ. ᴛʀᴇᴀᴛ ɪᴛ ᴡᴇʟʟ.**",
         "**❅ ʟɪғᴇ ɪs ᴡʜᴀᴛ ᴏᴜʀ ғᴇᴇʟɪɴɢs ᴅᴏ ᴡɪᴛʜ ᴜs.**",
         "**❅ ᴡʀɪɴᴋʟᴇs ᴀʀᴇ ᴛʜᴇ ʟɪɴᴇs ᴏғ ʟɪғᴇ ᴏɴ ᴛʜᴇ ғᴀᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs ᴍᴀᴅᴇ ᴜᴘ ᴏғ sᴏʙs, sɴɪғғʟᴇs, ᴀɴᴅ sᴍɪʟᴇs.**",
         "**❅ ɴᴏᴛ ʟɪғᴇ, ʙᴜᴛ ɢᴏᴏᴅ ʟɪғᴇ, ɪs ᴛᴏ ʙᴇ ᴄʜɪᴇғʟʏ ᴠᴀʟᴜᴇᴅ.**",
         "**❅ ʏᴏᴜ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ʟɪғᴇ ʙʏ ᴄʜᴀɴɢɪɴɢ ʏᴏᴜʀ ʜᴇᴀʀᴛ.",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ᴡɪᴛʜᴏᴜᴛ ᴛʀᴜᴇ ғʀɪᴇɴᴅsʜɪᴘ.**",
         "**❅ ɪғ ʏᴏᴜ ᴀʀᴇ ʙʀᴀᴠᴇ ᴛᴏ sᴀʏ ɢᴏᴏᴅ ʙʏᴇ, ʟɪғᴇ ᴡɪʟʟ ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ ᴀ ɴᴇᴡ ʜᴇʟʟᴏ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs ɴᴏᴛʜɪɴɢ ᴍᴏʀᴇ ᴇxᴄɪᴛɪɴɢ ɪɴ ᴛʜᴇ ᴡᴏʀʟᴅ, ʙᴜᴛ ᴘᴇᴏᴘʟᴇ.**",
         "**❅ ʏᴏᴜ ᴄᴀɴ ᴅᴏ ᴀɴʏᴛʜɪɴɢ, ʙᴜᴛ ɴᴏᴛ ᴇᴠᴇʀʏᴛʜɪɴɢ.**",
         "**❅ ʟɪғᴇ ʙᴇᴄᴏᴍᴇ ᴇᴀsʏ ᴡʜᴇɴ ʏᴏᴜ ʙᴇᴄᴏᴍᴇ sᴛʀᴏɴɢ.**",
         "**❅ ᴍʏ ʟɪғᴇ ɪsɴ’ᴛ ᴘᴇʀғᴇᴄᴛ ʙᴜᴛ ɪᴛ ᴅᴏᴇs ʜᴀᴠᴇ ᴘᴇʀғᴇᴄᴛ ᴍᴏᴍᴇɴᴛs.**",
         "**❅ ʟɪғᴇ ɪs ɢᴏᴅ’s ɴᴏᴠᴇʟ. ʟᴇᴛ ʜɪᴍ ᴡʀɪᴛᴇ ɪᴛ.**",
         "**❅ ᴏᴜʀ ʟɪғᴇ ɪs ᴀ ʀᴇsᴜʟᴛ ᴏғ ᴏᴜʀ ᴅᴏᴍɪɴᴀɴᴛ ᴛʜᴏᴜɢʜᴛs.**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴍᴏᴛɪᴏɴ ғʀᴏᴍ ᴀ ᴅᴇsɪʀᴇ ᴛᴏ ᴀɴᴏᴛʜᴇʀ ᴅᴇsɪʀᴇ.**",
         "**❅ ᴛᴏ ʟɪᴠᴇ ᴍᴇᴀɴs ᴛᴏ ғɪɢʜᴛ.**",
         "**❅ ʟɪғᴇ ɪs ʟɪᴋᴇ ᴀ ᴍᴏᴜɴᴛᴀɪɴ, ɴᴏᴛ ᴀ ʙᴇᴀᴄʜ.**",
         "**❅ ᴛʜᴇ ᴡᴏʀsᴛ ᴛʜɪɴɢ ɪɴ ʟɪғᴇ ɪs ᴛʜᴀᴛ ɪᴛ ᴘᴀssᴇs.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ ɪғ ᴡᴇ ᴀʀᴇ sɪᴍᴘʟᴇ.**",
         "**❅ ᴀʟᴡᴀʏs ᴛʜɪɴᴋ ᴛᴡɪᴄᴇ, sᴘᴇᴀᴋ ᴏɴᴄᴇ.**",
         "**❅ ʟɪғᴇ ɪs sɪᴍᴘʟᴇ, ᴡᴇ ᴍᴀᴋᴇ ɪᴛ ᴄᴏᴍᴘʟɪᴄᴀᴛᴇᴅ.**",
         "**❅ ʟɪғᴇ ɪs ɴᴏᴛ ᴍᴜᴄʜ ᴏʟᴅᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴅᴇᴀᴛʜ.**",
         "**❅ ᴛʜᴇ sᴇᴄʀᴇᴛ ᴏғ ʟɪғᴇ ɪs ʟᴏᴡ ᴇxᴘᴇᴄᴛᴀᴛɪᴏɴs!**",
         "**❅ ʟɪғᴇ ɪs ᴀ ᴛᴇᴀᴄʜᴇʀ..,ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟɪᴠᴇ, ᴛʜᴇ ᴍᴏʀᴇ ᴡᴇ ʟᴇᴀʀɴ.**",
         "**❅ ʜᴜᴍᴀɴ ʟɪғᴇ ɪs ɴᴏᴛʜɪɴɢ ʙᴜᴛ ᴀɴ ᴇᴛᴇʀɴᴀʟ ɪʟʟᴜsɪᴏɴ.**",
         "**❅ ᴛʜᴇ ʜᴀᴘᴘɪᴇʀ ᴛʜᴇ ᴛɪᴍᴇ, ᴛʜᴇ sʜᴏʀᴛᴇʀ ɪᴛ ɪs.**",
         "**❅ ʟɪғᴇ ɪs ʙᴇᴀᴜᴛɪғᴜʟ ɪғ ʏᴏᴜ  ᴋɴᴏᴡ ᴡʜᴇʀᴇ ᴛᴏ ʟᴏᴏᴋ.**",
         "**❅ ʟɪғᴇ ɪs ᴀᴡᴇsᴏᴍᴇ ᴡɪᴛʜ ʏᴏᴜ ʙʏ ᴍʏ sɪᴅᴇ.**",
         "**❅ ʟɪғᴇ – ʟᴏᴠᴇ = ᴢᴇʀᴏ**",
         "**❅ ʟɪғᴇ ɪs ғᴜʟʟ ᴏғ sᴛʀᴜɢɢʟᴇs.**",
         "**❅ ɪ ɢᴏᴛ ʟᴇss ʙᴜᴛ ɪ ɢᴏᴛ ʙᴇsᴛ **",
         "**❅ ʟɪғᴇ ɪs 10% ᴡʜᴀᴛ ʏᴏᴜ ᴍᴀᴋᴇ ɪᴛ, ᴀɴᴅ 90% ʜᴏᴡ ʏᴏᴜ ᴛᴀᴋᴇ ɪᴛ.**",
         "**❅ ᴛʜᴇʀᴇ ɪs sᴛɪʟʟ sᴏ ᴍᴜᴄʜ ᴛᴏ sᴇᴇ**",
         "**❅ ʟɪғᴇ ᴅᴏᴇsɴ’ᴛ ɢᴇᴛ ᴇᴀsɪᴇʀ ʏᴏᴜ ɢᴇᴛ sᴛʀᴏɴɢᴇʀ.**",
         "**❅ ʟɪғᴇ ɪs ᴀʙᴏᴜᴛ ʟᴀᴜɢʜɪɴɢ & ʟɪᴠɪɴɢ.**",
         "**❅ ᴇᴀᴄʜ ᴘᴇʀsᴏɴ ᴅɪᴇs ᴡʜᴇɴ ʜɪs ᴛɪᴍᴇ ᴄᴏᴍᴇs.**",
        ]

SHAYARI = [ " 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** ",
           " 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
           " 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀** ",
           " 🌺**काश वो दिन जल्दी आए,जब तू मेरे साथ सात फेरो में बन्ध जाए।**🌺 \n\n**🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀** ",
           " 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** ",
           " 🌺**महादेव ना कोई गाड़ी ना कोई बंगला चाहिए सलामत रहे मेरा प्यार बस यही दुआ चाहिए।**🌺 \n\n**🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀** ",
           " 🌺**फिक्र तो होगी ना तुम्हारी इकलौती मोहब्बत हो तुम मेरी।**🌺 \n\n**🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀** ",
           " 🌺**सुनो जानू आप सिर्फ किचन संभाल लेना आप को संभालने के लिए मैं हूं ना।**🌺 \n\n**🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀** ",
           " 🌺**सौ बात की एक बात मुझे चाहिए बस तेरा साथ।**🌺 \n\n**🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀** ",
           " 🌺**बहुत मुश्किलों से पाया हैं तुम्हें, अब खोना नहीं चाहते,कि तुम्हारे थे तुम्हारे हैं अब किसी और के होना नहीं चाहते।**🌺 \n\n**🥀Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.🥀** ",
           " 🌺**बेबी बातें तो रोज करते है चलो आज रोमांस करते है।**🌺 \n\n**🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀** ",
           " 🌺**सुबह शाम तुझे याद करते है हम और क्या बताएं की तुमसे कितना प्यार करते है हम।**🌺 \n\n**🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀** ",
           " 🌺**किसी से दिल लग जाने को मोहब्बत नहीं कहते जिसके बिना दिल न लगे उसे मोहब्बत कहते हैं।**🌺 \n\n**🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀** ",
           " 🌺**मेरे दिल के लॉक की चाबी हो तुम क्या बताएं जान मेरे जीने की एकलौती वजह हो तुम।**🌺 \n\n**🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀** ",
           " 🌺**हम आपकी हर चीज़ से प्यार कर लेंगे, आपकी हर बात पर ऐतबार कर लेंगे, बस एक बार कह दो कि तुम सिर्फ मेरे हो, हम ज़िन्दगी भर आपका इंतज़ार कर लेंगे।**🌺 \n\n**🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀** ",
           " 🌺**मोहब्बत कभी स्पेशल लोगो से नहीं होती जिससे होती है वही स्पेशल बन जाता है।**🌺 \n\n**🥀Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.🥀**",
           " 🌺**तू मेरी जान है इसमें कोई शक नहीं तेरे अलावा मुझ पर किसी और का हक़ नहीं।**🌺 \n\n**🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀** ",
           " 🌺**पहली मोहब्बत मेरी हम जान न सके, प्यार क्या होता है हम पहचान न सके, हमने उन्हें दिल में बसा लिया इस कदर कि, जब चाहा उन्हें दिल से निकाल न सके।**🌺 \n\n**🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀** ",
           " 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** ",
           " 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** ",
           " 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** ",
           " 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀** ",
           " 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** ",
           " 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** ",
           " 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀** ",
           " 🌺**देख के हमें वो सिर झुकाते हैं। बुला के महफिल में नजर चुराते हैं। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀** ",
           " 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** ",
           " 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** ",
           " 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** ",
           " 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** ",
           " 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀** ",
           " 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀** ",
           " 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀** ",
           " 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀** ",
           " 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद आएगी.**🌺\n\n**🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀** ",
           " 🌺**प्यार किया तो उनकी मोहब्बत नज़र आई दर्द हुआ तो पलके उनकी भर आई दो दिलों की धड़कन में एक बात नज़र आई दिल तो उनका धड़का पर आवाज़ इस दिल की आई.**🌺\n\n**🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀** ",
           " 🌺**कई चेहरे लेकर लोग यहाँ जिया करते हैं हम तो बस एक ही चेहरे से प्यार करते हैं ना छुपाया करो तुम इस चेहरे को,क्योंकि हम इसे देख के ही जिया करते हैं.**🌺\n\n**🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀** ",
           " 🌺**सबके bf को अपनी gf से बात करके नींद आजाती है और मेरे वाले को मुझसे लड़े बिना नींद नहीं आती।**🌺\n\n**🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀** ",
           " 🌺**सच्चा प्यार कहा किसी के नसीब में होता है. एसा प्यार कहा इस दुनिया में किसी को नसीब होता है.**🌺\n\n**🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀** " 
           ]

TAG_ALL = [ 
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢🥱 ",
           " 𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢 ",
           " 𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐑𝐨𝐦𝐚𝐧𝐭𝐢𝐜 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃 ",
           " 𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁🥲 ",
           " 𝐔𝐟𝐟 𝐊𝐲𝐚 𝐦𝐚𝐚𝐥 𝐡𝐚𝐢 𝐲𝐚𝐚𝐫 😁😂🥺 ",
           " 𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡a 𝐓𝐡a 𝐀𝐚𝐩𝐤𝐨 𝐛𝐚𝐭𝐡𝐫𝐨𝐨𝐦 𝐦𝐞 🤭 ",
           " 𝐎𝐲𝐞 𝐃𝐌 𝐊𝐚𝐫𝐨 𝐀𝐩𝐤𝐚 𝐦𝐨𝐨𝐝 𝐛𝐧𝐚 𝐝𝐞𝐭𝐢 𝐡𝐮 😅😅 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 ??🙂 ",
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢🥲 ",
           " 𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅😋 ",
           " 𝐎𝐲𝐲 𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐛𝐞𝐝𝐫𝐨𝐨𝐦 𝐦𝐞 𝐤𝐢𝐝𝐧𝐞𝐩 𝐤𝐚𝐫 𝐥o😅😅  ",
           " 𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅 ",
           " 𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁🤔 ",
           " 𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐉𝐀𝐍𝐄𝐌𝐀𝐍 🙄🙄 ",
           " 𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁 😁😕 ",
           " 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)🙃 ",
           " 𝐎𝐲𝐲 𝐏𝐫𝐢𝐲𝐚 𝐁𝐡𝐚𝐛𝐡𝐢 𝐤𝐚 𝐤𝐲𝐚 𝐡𝐚𝐢 😁😁😛 ",
           " 𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔 ",
           " 𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨 😅 ",
           " 𝐂𝐡𝐥𝐨 𝐇𝐚𝐦 𝐝𝐨𝐧𝐨 𝐫𝐚𝐭 𝐛𝐚𝐥𝐚.𝐠𝐚𝐧𝐞 𝐤𝐡𝐚𝐭𝐞 𝐡𝐚𝐢 😁.🤗 ",
           " 𝐂𝐡𝐚𝐥𝐨 𝐡𝐚𝐦 𝐝𝐨𝐧𝐨 𝐫𝐨𝐦𝐚𝐧𝐭𝐢𝐜 𝐛𝐚𝐭𝐞 𝐤𝐚𝐫𝐭𝐞 𝐡𝐚𝐢 😇 ",
           " 𝐨𝐨𝐲 𝐦𝐞𝐫𝐢 𝐡𝐞𝐥𝐩 𝐤𝐚𝐫𝐨𝐠𝐞 𝐦𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐞 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 😁🤭 ",
           " 𝐎𝐲𝐲 𝐭𝐮 𝐢𝐭𝐧𝐢 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐚𝐢 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐚𝐢 𝐡𝐢𝐥𝐚 𝐥𝐮 😁😀🥺🥺 ",
           " 𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐥𝐠𝐭𝐞 𝐡𝐨 𝐚𝐩😶 ",
           " 𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔 ",
           " 𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅😜 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 🙂🙂 ",
           " 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁😪 ",
           " 𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡 𝐉𝐀𝐍𝐄𝐌𝐀𝐍☺ ",
           " 𝐇𝐞𝐥𝐥𝐨 𝐀𝐩𝐤𝐚 𝐛𝐫𝐞𝐚𝐤 𝐮𝐩 𝐤𝐚𝐫𝐛𝐚 𝐝𝐞𝐭𝐚 𝐡𝐮 𝐚𝐩 𝐦𝐞𝐫𝐞 𝐬𝐞 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐥𝐨 😀😁🙊 ",
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😺 ",
           " 𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨🥲 ",
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😅 ",
           " 𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢😅 ",
           " 𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁😆😆😆 ",
           " 𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉 ",
           " 𝐀𝐚𝐣 𝐓𝐮𝐦 𝐟𝐢𝐧𝐠𝐞𝐫 𝐬𝐞 𝐡𝐢 𝐤𝐚𝐚𝐦 𝐜𝐡𝐚𝐥𝐚𝐨. 𝐆𝐡𝐚𝐫 𝐦𝐞 𝐛𝐚𝐢𝐠𝐚𝐧 𝐨𝐫 𝐦𝐮𝐤𝐢 𝐤𝐡𝐚𝐭𝐚𝐦 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐚𝐢 🙈🙈🙈 ",
           " 𝐎𝐲𝐲 𝐏𝐫𝐢𝐲𝐚 𝐁𝐡𝐚𝐛𝐡𝐢 𝐤𝐚 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐚𝐢 😁😁👀 ",
           " 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)😹 ",
           " 𝐨 𝐡𝐞𝐥𝐥𝐨 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐥𝐠𝐭𝐞 𝐡𝐨 𝐚𝐩😻 ",
           " 𝐓𝐮𝐦 𝐫𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 , 𝐁𝐡𝐮𝐭 𝐩𝐚𝐭𝐤𝐞 𝐡𝐢 𝐠𝐲𝐞 𝐡𝐨 💕😴🙃 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 .??😕 ",
           " 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀)🙃 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀?🙃 ",
           " 𝐉𝐡𝐚𝐭𝐞 𝐧𝐚 𝐜𝐡*𝐜*𝐈 𝐨𝐫 𝐛𝐚𝐭𝐞 𝐮𝐜𝐡𝐢 𝐮𝐜𝐡𝐢 😴😴😅 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮 .??🙂🧐 ",
           " 𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞.𝐏𝐥𝐳 𝐦𝐮𝐭𝐡 𝐦𝐚𝐫 𝐝𝐨😁😁.? ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀😠 ",
           " 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁❤ ",
           " 𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨👱 ",
           " 𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐚𝐢𝐬𝐢 𝐡𝐚𝐢🤧❣️ ",
           " 𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨😏😏 ",
           " 𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 𝐤𝐚𝐫𝐧𝐚 𝐡𝐢🤐 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀😒 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😮😮 "
           " 𝐉𝐡𝐚𝐭𝐞 𝐧𝐚 𝐜𝐡*𝐜*𝐈 𝐨𝐫 𝐛𝐚𝐭𝐞 𝐮𝐜𝐡𝐢 𝐮𝐜𝐡𝐢 😴😴😅👀 ", 
           " 𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 M𝐚𝐫𝐧𝐚 𝐡ai 😅😅 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅🥺🥺 ",
           " 𝐎𝐲𝐲 𝐬𝐮𝐧𝐨 𝐀𝐩 𝐑𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 𝐩𝐚𝐭𝐥𝐞 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐨👀 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀🙂 ",
           " 𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞?🤔** ",
           " 𝐤𝐚 𝐡𝐨 𝐤𝐚𝐫𝐞𝐣𝐚 1 𝐜𝐡𝐮𝐦𝐦𝐚 𝐧𝐚 𝐝𝐞𝐛𝐮 😅..🥺 ",
           " 𝐓𝐮𝐦 𝐫𝐨𝐣 𝐡𝐢𝐥𝐚𝐭𝐞 𝐡𝐨 𝐤𝐲𝐚 , 𝐁𝐡𝐮𝐭 𝐩𝐚𝐭𝐤𝐞 𝐡𝐢 𝐠𝐲𝐞 𝐡𝐨 💕😴🥺🥺 ",
           " 𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚 Bathroom me 🤭😅 ",
           " 𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞😁😁**",
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢👀 ",
           " 𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞.𝐇𝐢𝐥𝐥𝐚 𝐇𝐢𝐥𝐥𝐚 𝐤𝐞 𝐭𝐡𝐚𝐤 𝐠𝐲𝐚 𝐡𝐮😼 ",
           " 𝐎𝐲𝐲 𝐭𝐞𝐫𝐞 𝐛𝐚𝐥𝐞 𝐤𝐨 𝐣𝐚𝐤𝐚𝐫 𝐛𝐚𝐭𝐚𝐭𝐚 𝐡𝐮 𝐭𝐮 𝐲𝐡𝐚 𝐬𝐞𝐭𝐭𝐢𝐧𝐠 𝐤𝐚𝐫 𝐫𝐡𝐢 𝐡𝐚𝐢😸 ",
           " 𝐓𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐭𝐮𝐦𝐡𝐚𝐫𝐚 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨𝐭𝐚 𝐡𝐚𝐢 𝐤𝐲𝐚 😁🙈 ",
           " 𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅✌️🤞 ",
           " 𝐲𝐨𝐮𝐫 𝐟𝐚𝐯𝐨𝐮𝐫𝐢𝐭𝐞 𝐚𝐜𝐭𝐫𝐞𝐬𝐬 (𝐒𝐔𝐍𝐍𝐘 𝐋𝐄𝐎𝐍𝐄, 𝐨𝐫 𝐌𝐈𝐘𝐀 𝐊𝐇𝐀𝐋𝐈𝐅𝐀) 🥰 ",
           " 𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰 𝐌𝐚𝐬𝐭𝐞𝐫𝐛𝐚𝐭𝐢𝐧𝐠 𝐤𝐚𝐫𝐧𝐞 𝐦𝐞 𝐡𝐞𝐥𝐩 𝐡𝐨 𝐣𝐚𝐲𝐞𝐠𝐢 𝐦𝐞𝐫𝐢 😁 😁.🥺🥺 ",
           " 𝐁𝐡𝐚𝐛𝐡𝐢 𝐣𝐢 𝐤𝐨 𝐤𝐡𝐮𝐬𝐡 𝐫𝐤𝐡𝐚 𝐤𝐚𝐫𝐨 𝐭𝐡𝐚𝐧𝐝𝐢 𝐦𝐞 𝐰𝐚𝐫𝐧𝐚 𝐤𝐢𝐬𝐢 𝐨𝐫 𝐤𝐞 𝐬𝐚𝐭𝐡 𝐛𝐡𝐚𝐠 𝐣𝐚𝐲𝐞𝐠𝐢 😅😀😀🥲 ",
           " 𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉 ",
           " 𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁😋🥳 ",
           " 𝐔𝐟𝐟 𝐊𝐲𝐚 𝐦𝐚𝐚𝐥 𝐡𝐚𝐢 𝐲𝐚𝐚𝐫 DEKH KE KHADA HO GYA 😁😂🧐 ",
           " 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁🥺 ",
           " 𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁 😊 ",
           " 𝐀𝐩𝐤𝐢 𝐞𝐤 𝐩𝐢𝐜 𝐦𝐢𝐥𝐞𝐠𝐢 𝐤𝐲𝐚 𝐢𝐦𝐚𝐠𝐢𝐧𝐞 𝐤𝐚𝐫 𝐤𝐞 𝐦*𝐭𝐡 m𝐚𝐫𝐧𝐚 𝐡𝐢🥺🥺 ", 
           " 𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅😗 ",
           " 𝐚𝐩𝐤𝐢 𝐚𝐠𝐞 𝐤𝐲𝐚 𝐡𝐚𝐢 𝐡𝐨𝐭 𝐡𝐨 𝐚𝐩 𝐝𝐞𝐤𝐡𝐭𝐞 𝐡𝐢 𝐦𝐚𝐧 𝐤𝐚𝐫𝐭𝐚 𝐡𝐢𝐥𝐚𝐭𝐞 𝐫𝐡𝐮😁🥺 ",
           " 𝐀𝐚𝐣 𝐓𝐮𝐦 𝐟𝐢𝐧𝐠𝐞𝐫 𝐬𝐞 𝐡𝐢 𝐤𝐚𝐚𝐦 𝐜𝐡𝐚𝐥𝐚𝐨. 𝐆𝐡𝐚𝐫 𝐦𝐞 𝐛𝐚𝐢𝐠𝐚𝐧 𝐨𝐫 𝐦𝐮𝐤𝐢 𝐤𝐡𝐚𝐭𝐚𝐦 𝐡𝐨 𝐠𝐲𝐞 𝐡𝐚𝐢 😁🥰 ",
           " 𝐍𝐚 𝐉𝐚𝐦𝐢𝐧 𝐏𝐞 𝐍𝐚 𝐀𝐬𝐡𝐦𝐚𝐧 𝐩𝐞 𝐓𝐞𝐫𝐢 𝐆𝐝 𝐦𝐚𝐫𝐮𝐧𝐠𝐚 𝐚𝐩𝐧𝐞 𝐁𝐡𝐚𝐢 𝐤𝐞 𝐦𝐚𝐤𝐚𝐧 𝐩𝐞😜** ",
           " 𝐎𝐲𝐲 𝐢𝐭𝐧𝐚 𝐡𝐨𝐭 𝐤𝐲𝐮 𝐡𝐨 𝐭𝐮𝐦 𝐝𝐞𝐤𝐡 𝐤𝐞 𝐤𝐡𝐚𝐝𝐚 𝐡𝐨 𝐣𝐚𝐭𝐚 𝐡𝐚𝐢 😂 𝐑𝐨𝐧𝐠𝐭𝐞😁😁😁🥰 ",
        ]


async def is_user_admin(client, chat_id, user_id):
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)
    except UserNotParticipant:
        return False


@app.on_message(filters.command(["gntag"], prefixes=["/", "!"]))
async def mention_all_gn(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(GN_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["gmtag"], prefixes=["/", "!"]))
async def mention_all_gm(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(GM_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["hitag"], prefixes=["/", "!"]))
async def mention_all_hi(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(HI_MESSAGES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["lifetag"], prefixes=["/", "!"]))
async def mention_all_quotes(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(QUOTES)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["shayari"], prefixes=["/", "!"]))
async def mention_all_shayari(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(SHAYARI)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["tagall"], prefixes=["/", "!"]))
async def mention_all_tagall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")

    spam_chats.append(chat_id)
    try:
        async for member in client.get_chat_members(chat_id):
            if not chat_id in spam_chats:
                break
            if member.user.is_bot:
                continue
            await client.send_message(
                chat_id,
                f"[{member.user.first_name}](tg://user?id={member.user.id}) {random.choice(TAG_ALL)}"
            )
            await asyncio.sleep(4)
    finally:
        if chat_id in spam_chats:
            spam_chats.remove(chat_id)

@app.on_message(filters.command(["gmstop", "gnstop", "histop", "lifestop", "shayarioff", "tagoff", "tagstop"], prefixes=["/", "!"]))
async def cancel_mention(client, message):
    chat_id = message.chat.id
    if not chat_id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")

    if not await is_user_admin(client, chat_id, message.from_user.id):
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")

    spam_chats.remove(chat_id)
    await message.reply("๏ 🦋ᴍᴇɴᴛɪᴏɴ ʀᴏᴋɴᴇ ᴡᴀʟᴇ ᴋɪ ᴍᴀᴀ ᴋᴀ ʙʜᴀʀᴏsᴀ ᴊᴇᴇᴛᴜ.....🫠 ๏")