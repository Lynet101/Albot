#[descord::event]
pub async fn ready(ready: ReadyData) {
    println!(
        "Logged in as: {}#{}",
        ready.user.username, ready.user.discriminator
    );
}