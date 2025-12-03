
                        now = datetime.datetime.now()
                        time_str = now.strftime(" %Hh %Mp %Y-%m-%d")
                        app_drive.img(time_str)
                        if os.path.exists(time_str + '.jpg'):
                                        os.remove(time_str + '.jpg')