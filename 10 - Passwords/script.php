#!/usr/bin/env php
<?php

# Usage:
#  generate-password.php <secret1> <secret2> <times> <user_id> <old_hash>

$secret1 = (int)$argv[1];
$secret2 = (int)$argv[2];

if (!isset($argv[5])) {
  # First password for this user
  $secret3 = $argv[4];
} else {
  # Existing user, password reset
  $secret3 = $argv[5];
}

$times = (int)$argv[3];

for ($t=0; $t<$times; $t++) {
  $secret3 = crc32($secret3);
  $counter = ($secret3 * bcpowmod($secret1, 10000000, $secret2)) % $secret2;

  $password = "";
  for ($i=0; $i<10; $i++) {
    # Generate random passwords
    $counter = ($counter * $secret1) % $secret2;
    $password .= chr($counter % 94 + 33);
  }

  $hash = md5($password);
  $secret3 = $hash;
}

echo "$password $hash\n";
