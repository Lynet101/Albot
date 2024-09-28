mod sub_routines;
#[descord::slash]
pub async fn group_delete(message: Interaction, guild_id: u64, name: String, members: String){
    delete_role(message, guild_id, name).await;
    delete_channels(message, guild_id, name).await;
}