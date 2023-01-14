lang = "简体中文"
def get(thing: str):
    objects = {
        "English": {
            "Main.Notebook.Launch": "Launch game",
            "Main.Notebook.Download": "Downloads",
            "Main.Notebook.Option": "Options",
            "Main.Notebook.About": "About FMCL",
            "Main.Notebook.Mods": "Mods download",
            "Main.Notebook.Accounts": "Accounts",
            "Main.Notebook.Gaming": "Multiplayer",
            "Account.OpenURL": "Open link",
            "Account.Auth": "Login",
            "Account.AboutMicrosoft": "Add Microsoft Account",
            "Account.Offline": "Add Offline account",
            "Account.Help": "I need help",
            "Account.HelpText": "If you want to add a Microsoft Account，Please click [Open link]. Then, Input redirect link to the input box. Finally, click [Login]\n"
                                "If you don't have a Microsoft Account，You can input username in the input box below，Click [Add] to use offline account",
            "Account.Add": "Add",
            "Account.Success": "Successfully added account!",
            "Account.Fail": "Failed to add account",
            "Account.Have": "My accounts",
            "Account.Delete": "Delete",
            "Launch.Choose": "Choose game version",
            "Launch.Account": "Choose gaming account",
            "Launch.Launch": "Launch",
            "Launch.Ask": "Are you sure to launch the game?",
            "Launch.Error": "Game exited unexpectedly，Error code",
            "Launch.ErrorText": "Game exited unexpectedly，Please send FMCL.log to others who can help you.",
            "Launch.Wait": "Please wait for the game window to appear，Then enjoy Minecraft！"
        },
        "简体中文": {
            "Main.Notebook.Launch": "启动游戏",
            "Main.Notebook.Download": "下载游戏",
            "Main.Notebook.Option": "启动器设置",
            "Main.Notebook.About": "关于FMCL",
            "Main.Notebook.Mods": "模组下载",
            "Main.Notebook.Accounts": "账户管理",
            "Main.Notebook.Gaming": "多人联机",
            "Account.OpenURL": "打开登录网址",
            "Account.Auth": "登录",
            "Account.AboutMicrosoft": "添加微软账号",
            "Account.Offline": "添加离线账号",
            "Account.Help": "我需要帮助",
            "Account.HelpText": "若要添加微软账户，请点击[打开登陆网址]，将重定向链接输入到文本框，点击[登录]\n"
                                "若没有微软账户，可以在下面的文本框输入玩家名，点击[创建]来使用离线账户",
            "Account.Add": "添加",
            "Account.Success": "成功添加账户",
            "Account.Fail": "添加账户失败",
            "Account.Have": "我拥有的账户",
            "Account.Delete": "删除",
            "Launch.Choose": "选择游戏版本",
            "Launch.Account": "选择游戏账户",
            "Launch.Launch": "启动",
            "Launch.Ask": "确定启动游戏吗？",
            "Launch.Error": "游戏意外退出，错误码",
            "Launch.ErrorText": "游戏意外退出，请将FMCL.log发给他人寻求帮助",
            "Launch.Wait": "请耐心等待游戏窗口出现，然后畅玩Minecraft吧！"
        }
    }
    return objects[lang][thing]