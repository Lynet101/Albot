mod sub_routines;
#[descord::slash]
pub async fn group_create(message: Interaction, guild_id: u64, name: String, members: String){
    create_role(message, guild_id, name).await;
    create_channels(message, guild_id, name).await;
    add_members_to_role(message, guild_id, name, members).await;
}