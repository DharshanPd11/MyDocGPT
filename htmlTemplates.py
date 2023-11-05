css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fps.w.org%2Fone-user-avatar%2Fassets%2Ficon-256x256.png%3Frev%3D2536829&tbnid=-Bi_x5cMoXJwoM&vet=12ahUKEwjDl_KJ9ayCAxVioekKHQ9LBmUQMyhEegUIARDtAQ..i&imgrefurl=https%3A%2F%2Fwordpress.org%2Fplugins%2Fone-user-avatar%2F&docid=eHY2av3Fm98pBM&w=256&h=256&q=user%20png&hl=en&ved=2ahUKEwjDl_KJ9ayCAxVioekKHQ9LBmUQMyhEegUIARDtAQ" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
