import subprocess

def generate_notification(title, notification):
    script = rf'''
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime] > $null
        $template = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText01)
        $template.GetElementsByTagName("text")[0].AppendChild($template.CreateTextNode("{notification}")) > $null
        $toast = [Windows.UI.Notifications.ToastNotification]::new($template)
        $notifier = [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("{title}")
        $notifier.Show($toast)
    '''

    subprocess.run([
        'powershell',
        '-NoProfile',
        '-ExecutionPolicy', 'Bypass',
        '-Command', script
    ])