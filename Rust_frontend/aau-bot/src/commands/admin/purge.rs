use crate::types::{Error, Context};
use serenity::model::channel::Message;
use serenity::prelude::*;

#[poise::command(slash_command)]
pub async fn purge(ctx: Context<'_>, amount: u32) -> Result<(), Error> {
    let channel_id = ctx.channel_id();
    
    // Fetch the last N messages
    let messages = channel_id
        .messages(&ctx.http(), |m| m.limit(amount))
        .await?;

    // Delete the fetched messages
    channel_id.delete_messages(&ctx.http(), &messages.iter().map(|m| m.id)).await?;

    ctx.say(format!("Deleted {} messages.", amount)).await?;
    
    Ok(())
}
