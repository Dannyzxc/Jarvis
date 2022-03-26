#regular_expressions_to_search_and_find

my_file = '''

name = $_POST['name'];
visitor_email = POST['email'];$subject = POST['subject'];
$message =POST['message'];
$email_from = 'dnyaneshwar1997g@gmail.com';

email_subject = 'New Form Submission';

email_body= "User Name:$name.\n".
                "User Name:$visitor_email.\n".
                "Subject: $subject.\n".
                "User Message:$message .\n";

to = 'dnyane.04@gmail.com';

headers = "from: email_from \r\n";
headers .= "Reply-To: visitor_email \r\n";

mail($to,$email_subject,email_body,$headers);

header("Location: contact.html");
9763121498
'''

import re
patt = re.compile(r'\d{10}')   # searching for word dnyane. from my_file or to . to search all
matches = patt.finditer(my_file)
for match in matches:
    print(match)

print(my_file[364:371])   # 364: 371 is word location

# to check more search re module