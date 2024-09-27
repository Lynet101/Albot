//use crate::commands::group::{};
use crate::types::{Error, Context};

#[poise::command(prefix_command, slash_command, subcommands())]
pub async fn group(_ctx: Context<'_>) -> Result<(), Error> {
    Ok(())
}