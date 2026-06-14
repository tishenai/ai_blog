---
title: 'Postflight E2E 测试草稿 215111'
date: '2026-06-14 21:55:00'
tags:
  - 测试
categories:
  - 测试
thumbnail: /images/thumbnails/postflight-e2e-test-20260614215111.png
showLicense: false
showComments: true
---

这是一篇用于测试 daily-ai-blog-postflight 的临时草稿。

如果 postflight 正常，它应该：

1. 在飞书知识库创建 Draft 审稿文档；
2. 刷新知识库首页；
3. 给 owner 发送审稿通知；
4. 在 .daily_ai_blog_review_notified.json 中记录通知状态；
5. 最终 audit 通过。
