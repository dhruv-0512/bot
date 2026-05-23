function ask {
    param([string]$msg)
    $res = irm https://my-bot.onrender.com/chat `
        -Method POST `
        -ContentType "application/json" `
        -Body "{`"message`": `"$msg`"}"
    Write-Host "`nBot: $($res.reply)`n"
}
Write-Host "CS Bot ready. Usage: ask 'your question'"