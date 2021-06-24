const userbot = require("./userbot");
const bot = require("vcbot/bot");

(async () => {
  await userbot.start();
  await bot.start();
})();
