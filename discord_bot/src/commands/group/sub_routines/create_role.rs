pub async fn create_role(message: Interaction, guild_id: u64, name: &str) -> Result<Role, Box<dyn std::error::Error>> {
    match create_role(&message.http, guild_id, name).await {
        Ok(role) => {
            if let Err(why) = message.channel_id.say(&message.http, format!("Role '{}' created with ID: {}", role.name, role.id)).await {
                println!("Error sending message: {:?}", why);
            }
        }
        Err(why) => {
            println!("Error creating role: {:?}", why);
        }
    }
}