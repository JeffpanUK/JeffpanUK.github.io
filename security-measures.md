# 安全措施说明

## EmailJS 安全优化

### 当前已实现的安全措施

#### 1. 密钥混淆
- 使用 Base64 编码存储密钥
- 在运行时解码使用
- 提供简单的安全保护

#### 2. 内容安全策略 (CSP)
```html
<meta http-equiv="Content-Security-Policy" content="
    default-src 'self';
    script-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net;
    style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
    font-src 'self' https://fonts.gstatic.com;
    img-src 'self' data:;
    connect-src 'self' https://api.emailjs.com;
">
```

#### 3. 额外安全特性
- 防止内容类型混淆攻击
- 防止点击劫持攻击
- 防止 XSS 攻击
- 限制引用策略

### 建议的进一步安全措施

#### 1. IP 白名单
在 EmailJS 控制台中配置允许的域名，只接受来自 `jeffpan.net` 的请求。

#### 2. 表单验证强化
```javascript
// 添加简单的验证码
function getHoneypot() {
    const timestamp = Date.now() / 1000;
    const signature = btoa(timestamp + '|' + 'secret_salt');
    return signature;
}
```

#### 3. 服务器端验证
使用 Cloud Functions 或其他后端服务验证请求的合法性。

#### 4. 限制请求频率
```javascript
let lastSubmitTime = 0;
const MIN_INTERVAL = 30000; // 30 秒

function canSubmit() {
    const now = Date.now();
    if (now - lastSubmitTime > MIN_INTERVAL) {
        lastSubmitTime = now;
        return true;
    }
    return false;
}
```

### EmailJS 安全最佳实践

#### 1. 理解 EmailJS 的工作原理
- EmailJS 使用公钥和私钥相结合的方法
- 公钥是安全的，但不应被滥用
- 私钥绝对不能在前端暴露

#### 2. 配置您的 EmailJS 账户
1. 在 EmailJS 控制台中：
   - 点击您的服务
   - 点击 "Settings"
   - 配置 "Allowed Origins"
2. 只允许 `https://jeffpan.net` 和 `http://localhost:*`
3. 考虑启用 reCAPTCHA 验证

#### 3. 使用环境变量
对于更安全的部署，可以使用：
```javascript
// 从环境变量获取配置
const USER_ID = process.env.EMAILJS_USER_ID;
const SERVICE_ID = process.env.EMAILJS_SERVICE_ID;
const TEMPLATE_ID = process.env.EMAILJS_TEMPLATE_ID;
```

#### 4. 定期更新您的安全配置
- 定期检查您的安全设置
- 更新您的密钥和密码
- 监控任何可疑活动

### 发生安全事件时的响应

1. **立即撤销密钥**：在 EmailJS 控制台中生成新的公钥
2. **检查日志**：查看 EmailJS 的发送日志以了解事件详情
3. **分析事件**：确定安全漏洞
4. **修复漏洞**：更新您的代码
5. **通知用户**：如果有敏感信息暴露，通知受影响的用户

### 资源

- EmailJS 安全文档：https://www.emailjs.com/docs/security/
- MDN 内容安全策略：https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
- 安全最佳实践：https://owasp.org/www-community/OWASP_Top_Ten
