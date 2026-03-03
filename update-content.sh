#!/bin/bash

# 个人网站内容更新脚本

# 项目根目录
PROJECT_DIR="/root/.openclaw/workspace/jeffpan.net"

# 检查项目目录
if [ ! -d "$PROJECT_DIR" ]; then
    echo "错误：项目目录 $PROJECT_DIR 不存在"
    exit 1
fi

# 切换到项目目录
cd "$PROJECT_DIR" || exit 1

# 更新脚本
echo "开始更新网站内容..."

# 更新 git
git config --global user.name "Jeff Pan"
git config --global user.email "2359501@qq.com"

# 检查远程仓库连接
if ! git remote -v > /dev/null; then
    echo "错误：无法检测到远程仓库"
    echo "请先按照 DEPLOYMENT.md 文件的说明创建和配置 GitHub 仓库"
    exit 1
fi

# 检查是否有未提交的更改
if ! git status | grep -q "nothing to commit"; then
    echo "检测到未提交的更改，正在提交..."
    git add .
    git commit -m "自动更新网站内容 $(date +"%Y-%m-%d %H:%M:%S")"
    
    # 尝试推送到远程仓库
    if git push; then
        echo "内容已成功更新并推送到远程仓库"
        echo "GitHub Pages 将在几分钟内自动部署更新后的内容"
    else
        echo "错误：无法推送到远程仓库"
        echo "请检查网络连接或尝试手动推送"
        exit 1
    fi
else
    echo "没有发现需要更新的内容"
    echo "如果您修改了内容但没有生效，请检查 git status"
fi

# 检查部署状态
echo "---"
echo "检查网站部署状态..."
echo "您的网站应该可以在以下地址访问："
echo "- 自定义域名：https://jeffpan.net"
echo "- GitHub Pages 地址：https://2359501.github.io/jeffpan.net"
echo "---"
echo "如果无法访问，请等待几分钟后再尝试"
echo "如果仍有问题，请按照 DEPLOYMENT.md 文件的说明进行检查"
