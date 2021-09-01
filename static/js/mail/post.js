let url = '127.0.0.1:8000/api/send-mail/'

function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

const csrftoken = getCookie('csrftoken');
document.getElementById("send").oncllick(()=>{

fetch(url, {
	method: 'POST',
	credentials: 'same-origin',
	headers:{
		'Accept': 'application/json',
		'X-Requested-With': 'XMLHttpRequest',
		'X-CSRFToken': csrftoken,
	},
	body: JSON.stringify({
		'sender': "{{user.email}}",
		'subject': document.getElementById("subjectfield").value,
		'body': document.getElementById("messagebody").innerHTML,
		'recipients_list': document.getElementById("recipientlabel").value,
		'send_on': document.getElementById("time").value,
		'attachment_file': document.getElementById("upload").value
	})
})
.then(response => { return response.json })
		
.then(data -> { console.log(data) })
})
