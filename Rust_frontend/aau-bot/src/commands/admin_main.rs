use crate::commands::admin::{echo, ping}; //, purge};
use crate::types::{Error, Context};

#[poise::command(prefix_command, slash_command, subcommands("echo::echo", "ping::ping"))]//, "purge::purge"))]
pub async fn admin(_ctx: Context<'_>) -> Result<(), Error> {
    Ok(())
}