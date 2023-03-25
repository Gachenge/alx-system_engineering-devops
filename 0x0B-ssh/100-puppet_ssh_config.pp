# code to bypass password
file{ '/home/victor/.ssh/config':
owner => 'victor',
group => 'victor',
mode => '0600',
content => "Host ubuntu\n\
            \tPasswordAuthentication no\n\
            \tIdentifyFile ~/.ssh/school\n",
}
