import pandas as pd

class Statistics:
    def __init__(self, player_name, player_age):
        self.player_name = player_name
        self.player_age = player_age
        self.games_played = 0
        self.skills = {
                        "Finish a connect four"             : 0,
                        "Block a connect four"              : 0,
                        "Setup trap"                        : 0,
                        "Do not fall for trap"              : 0,
                        "Block a trap"                      : 0,
                        "Setup unstoppable connect four"    : 0,
                        "Block unstoppable connect four"    : 0
                      }
        
        df = pd.read_csv('ConnectFour\saved_data\profiles.csv')
        try:
            profile = df[df['Player_name'] == player_name].values.tolist()[0]
            self.player_age = profile[1]
            self.games_played = profile[2]
            self.skills["Finish a connect four"         ]   = profile[3]
            self.skills["Block a connect four"          ]   = profile[4]
            self.skills["Setup trap"                    ]   = profile[5]
            self.skills["Do not fall for trap"          ]   = profile[6]
            self.skills["Block a trap"                  ]   = profile[7]
            self.skills["Setup unstoppable connect four"]   = profile[8]
            self.skills["Block unstoppable connect four"]   = profile[9]
            print(self.skills)
        except:
            pass

    def get_statistics(self):
        pass
    
    def add_game(self,stats):
        self.skills["Finish a connect four"         ]   += stats[0]
        self.skills["Block a connect four"          ]   += stats[1]
        self.skills["Setup trap"                    ]   += stats[2]
        self.skills["Do not fall for trap"          ]   += stats[3]
        self.skills["Block a trap"                  ]   += stats[4]
        self.skills["Setup unstoppable connect four"]   += stats[5]
        self.skills["Block unstoppable connect four"]   += stats[6]
        self.games_played += 1
        print(self.skills)

    def save_statistics(self):
        df = pd.read_csv('ConnectFour\saved_data\profiles.csv')
        if df.index[df["Player_name"]== self.player_name].size > 0:
            df.loc[df["Player_name"] == self.player_name, "Games_played"                    ] = self.games_played
            df.loc[df["Player_name"] == self.player_name, "Finish_a_connect_four"           ] = self.skills["Finish a connect four"]
            df.loc[df["Player_name"] == self.player_name, "Block_a_connect_four"            ] = self.skills["Block a connect four"]
            df.loc[df["Player_name"] == self.player_name, "Setup_trap"                      ] = self.skills["Setup trap"]
            df.loc[df["Player_name"] == self.player_name, "Do_not_fall_for_trap"            ] = self.skills["Do not fall for trap"]
            df.loc[df["Player_name"] == self.player_name, "Block_a_trap"                    ] = self.skills["Block a trap"]
            df.loc[df["Player_name"] == self.player_name, "Setup_unstoppable_connect_four"  ] = self.skills["Setup unstoppable connect four"]
            df.loc[df["Player_name"] == self.player_name, "Block_unstoppable_connect_four"  ] = self.skills["Block unstoppable connect four"]
            df.to_csv('ConnectFour\saved_data\profiles.csv',index=False)
        
        else:
            print("hallo")
            df.loc["Player_name", "Player_name"                     ] = self.player_name
            df.loc["Player_name", "Player_age"                      ] = self.player_age
            df.loc["Player_name", "Games_played"                    ] = self.games_played
            df.loc["Player_name", "Finish_a_connect_four"           ] = self.skills["Finish a connect four"]
            df.loc["Player_name", "Block_a_connect_four"            ] = self.skills["Block a connect four"]
            df.loc["Player_name", "Setup_trap"                      ] = self.skills["Setup trap"]
            df.loc["Player_name", "Do_not_fall_for_trap"            ] = self.skills["Do not fall for trap"]
            df.loc["Player_name", "Block_a_trap"                    ] = self.skills["Block a trap"]
            df.loc["Player_name", "Setup_unstoppable_connect_four"  ] = self.skills["Setup unstoppable connect four"]
            df.loc["Player_name", "Block_unstoppable_connect_four"  ] = self.skills["Block unstoppable connect four"]
            df.to_csv('ConnectFour\saved_data\profiles.csv',index=False)

