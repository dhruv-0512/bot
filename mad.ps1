while ($true) {
    $msg = Read-Host "You"
    if ($msg -eq "exit") { break }
    $res = irm https://bot-qrxb.onrender.com/chat `
        -Method POST `
        -ContentType "application/json" `
        -Body "{`"message`": `"$msg`"}"
    Write-Host "`nBot: $($res.reply)`n"
}