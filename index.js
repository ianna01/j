const input = require("input");
const { TelegramClient } = require("telegram");
const { StringSession } = require("telegram/sessions");

const apiId = Number(process.env.API_ID);
const apiHash = process.env.API_HASH;

(async () => {
    const client = new TelegramClient(
        new StringSession(""),
        apiId,
        apiHash,
        {
            connectionRetries: 5
        }
    );

    await client.start({
        phoneNumber: async () =>
            await input.text("Số điện thoại: "),

        password: async () =>
            await input.text("Mật khẩu 2FA: "),

        phoneCode: async () =>
            await input.text("Mã Telegram: "),

        onError: err =>
            console.error(err)
    });

    console.log("\n================================");
    console.log("SESSION CỦA BẠN:");
    console.log("================================\n");

    console.log(client.session.save());

    console.log("\n================================");

    await client.disconnect();
})();
