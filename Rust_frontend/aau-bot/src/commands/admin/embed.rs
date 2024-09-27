use crate::types::{Context, Error};

#[poise::command(slash_command)]
pub async fn embed(ctx: Context<'_>) -> Result<(), Error> {
}