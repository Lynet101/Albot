#[descord::slash]
pub async fn ping(interaction: Interaction) {
    interaction.reply("Pong!", true).await;
}