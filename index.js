const input = require("input");
const { TelegramClient } = require("telegram");
const { StringSession } = require("telegram/sessions");

const apiId = 37189725
const apiHash = "59edf8998a111263a171739eda971a50"

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
