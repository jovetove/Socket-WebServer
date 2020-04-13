from MethodStrategy import Context, POST, GET


class StrategyFactory:
    """简单工厂，负责创建具体的策略"""
    @staticmethod
    def choice_mothod(name: str) -> Context:
        if name == 'POST':
            return Context(POST())
        elif name == 'GET':
            return Context(GET())
        elif name == "delete":
            pass  # TODO
        elif name == "PUT":
            pass  # TODO
        else:
            raise ValueError("请求参数错误")