# find error and fix it

exec { 'delete letter':
    command => 'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
    provider => shell,
    }
