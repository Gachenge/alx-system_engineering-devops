# code to bypass password
file{ '/home/victor/.ssh/config':
owner => 'victor',
group => 'victor',
mode => '0600',
content => "Host ubuntu\n\
            \tIdentityFile ~/.ssh/school\n\
            \tPasswordAuthentication no\n",
}
