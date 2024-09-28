mod sub_routines;
#[descord::slash]
pub async fn group_add(message: Interaction, guild_id: u64, name: String, members: String){
    add_members_to_role(message, guild_id, name, members).await;
}