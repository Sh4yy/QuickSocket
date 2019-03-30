class Route:

    def __init__(self, callable=None):
        self._path = {}
        self.callable = callable

    def find(self, route, create=False):
        if not route:
            return self

        parent = self
        while True:
            if not route:
                return parent
            elif route[0] in parent._path:
                parent = parent._path[route[0]]
                route = route[1:]
                continue

            if create:
                parent._path[route[0]] = Route()
                parent = parent._path[route[0]]
                route = route[1:]
                continue

            return None

    def insert(self, routes, callable):
        path = self.find(routes, create=True)
        if not path:
            return False

        path.callable = callable
        return True

class RouteManager:

    def __init__(self):
        self._routes = Route()

    @staticmethod
    def _path_parser(path):
        path = path.strip('/')
        return path.split()

    def insert(self, path, callable):
        path = RouteManager._path_parser(path)
        if not path:
            self._routes.callable = callable
        else:
            self._routes.insert(path, callable)

    def delete(self, path):
        path = RouteManager._path_parser(path)
        if not path:
            return True
        else:
            sec = self._routes.find(path)
            if sec: del sec
            return True

    def get(self, path):
        path = RouteManager._path_parser(path)
        if not path:
            return None
        else:
            sec = self._routes.find(path)
            return sec.callable if sec else None

    def route(self, path):
        def decor(callable):
            self.insert(path, callable)
            return callable

        return decor
