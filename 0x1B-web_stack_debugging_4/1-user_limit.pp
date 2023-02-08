# Script to change the OS configuration to enable
# holberton user login and open files without error.

# Increase hard Holberton's file limit.
exec { 'increase-olherton-file-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase Holberton's soft file limit.
exec { 'increase-holberton-soft-file-limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
