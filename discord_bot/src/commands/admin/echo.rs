#[descord::slash]
pub async fn echo(interaction: Interaction, message: String) {
    interaction.reply(message, false).await;
}
