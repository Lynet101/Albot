use crate::types::{Error, Context};

#[poise::command(slash_command)]
pub async fn echo(ctx: Context<'_>, message: String) -> Result<(), Error> {
    ctx.say(message).await?;
    Ok(())
}