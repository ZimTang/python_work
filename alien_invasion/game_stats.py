class GamesStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.score = None
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_stats()
        # 任何情况下都不应重置最高得分。
        self.high_score = 0
        # 让游戏一开始处于非活动状态
        self.game_active = False

    def reset_stats(self):
        """初始化随游戏进行可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


