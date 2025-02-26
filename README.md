# Weather-API
Build a weather API that fetches and returns weather data.构建一个获取和返回天气数据的天气 API。

# 天气 API

构建一个获取和返回天气数据的天气 API。


在这个项目中，我们将构建一个天气 API，从第三方 API 获取和返回天气数据，而不是依赖我们自己的天气数据。此项目将帮助您了解如何使用第三方 API、缓存和环境变量。

![Weather API](https://assets.roadmap.sh/guest/weather-api-f8i1q.png)
至于实际使用的天气 API，你可以使用你最喜欢的一个，作为建议，这里有一个指向 [Visual Crossing 的 API](https://www.visualcrossing.com/weather-api) 的链接，它是完全免费且易于使用的。

关于内存缓存，一个非常常见的建议是使用 [Redis](https://redis.io/)，您可以[在此处](https://redis.io/docs/latest/develop/clients/client-side-caching/)阅读有关它的更多信息，作为建议，您可以使用用户输入的城市代码作为密钥，并将调用 API 的结果保存在那里。

同时，当您在缓存中 “设置” 值时，您还可以为其指定一个以秒为单位的过期时间（使用 `SET` 命令上的 `EX` 标志）。这样，当数据足够旧时（例如，给它 12 小时的过期时间），缓存（键)会自动清理自己。

------

## 一些提示

以下是一些帮助您入门的提示：

- 首先创建一个简单的 API，该 API 返回硬编码的天气响应。这将帮助您了解如何构建 API 以及如何处理请求。
- 使用环境变量存储 API 密钥和 Redis 连接字符串。这样，您可以轻松更改它们，而无需修改代码。
- 确保正确处理错误。如果第三方 API 已关闭，或者城市代码无效，请确保返回相应的错误消息。
- 使用一些包或模块来发出 HTTP 请求，例如，如果您使用的是 Node.js，则可以使用 `axios` 包，如果您使用的是 Python，则可以使用 `requests` 模块。
- 实施速率限制以防止滥用 API。如果您使用的是 Node.js，则可以使用 `express-rate-limit` 之类的包，如果您使用的是 Python，则可以使用 `flask-limiter` 之类的包。

此项目将帮助您了解如何使用第三方 API、缓存和环境变量。它还将帮助您了解如何构建 API 以及如何处理请求。

# 运行和测试
启动 Redis 服务（需要先安装 Redis）

在 PyCharm 中：

配置运行环境变量

右键运行 app.py

测试 API：

bash

curl "http://localhost:5000/weather?city=Beijing"
