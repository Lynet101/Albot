mod commands;
mod events;
use descord::prelude::*;
use crate::commands::admin::{echo, ping};
use events::ready;
use std::env;

#[tokio::main]
async fn main() {
    let token = env::var("DISCORD_TOKEN").expect("Expected a token in the environment");
    let mut client = Client::new(&token, GatewayIntent::ALL, "!").await;
    descord::register_all!(client => []);
    client.login().await;
}