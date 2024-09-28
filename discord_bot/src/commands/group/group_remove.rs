mod sub_routines;
#[descord::slash]
pub async fn group_remove(message: Interaction, guild_id: u64, name: String, members: String){
    remove_members_from_role(message, guild_id, name, members).await;
}