const { Composer } = require("grammy");
const connections = require("vcbot/connections");
const queues = require("vcbot/queues");

const composer = new Composer();

composer.on(":voice_chat_ended", async (ctx) => {
  connections.remove(ctx.chat.id);
  queues.clear(ctx.chat.id);
});

module.exports = composer;
