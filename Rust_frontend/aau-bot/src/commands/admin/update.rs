use crate::types::{Error, Context};

#[poise::command(slash_command)]
pub async fn update(ctx: Context<'_>, #[description = "Makes the bot say inputes message"] message: String) -> Result<(), Error> {
}