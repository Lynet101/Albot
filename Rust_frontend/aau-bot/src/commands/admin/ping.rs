use crate::types::{Error, Context};

#[poise::command(slash_command)]
pub async fn ping(ctx: Context<'_>) -> Result<(), Error> {
    ctx.say("pong!, I'm alive and rusty").await?;
    Ok(())
}
