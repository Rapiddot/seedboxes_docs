// src/theme/Root.js
import React, { useEffect, useRef } from "react";
// @ts-ignore
import Chatbot from "@site/static/js/n8n-embed.js";

export default function Root({ children }) {
  const ChatbotRef = useRef(null);
  const currentModeRef = useRef("light");
  const observerRef = useRef(null);

  // --- palettes aligned with your custom.css ---
  const buildTheme = (mode) => {
    const isDark = mode === "dark";
    return {
      button: {
        backgroundColor: isDark ? "#f6bb42" : "#f6bb42",
        right: 40,
        bottom: 40,
        size: 60,
        iconColor: isDark ? "#1c1c1c" : "#ffffff",
        customIconSrc: "https://www.svgrepo.com/show/339963/chat-bot.svg",
        customIconSize: 60,
        customIconBorderRadius: 15,
        autoWindowOpen: { autoOpen: false, openDelay: 2 },
        borderRadius: "rounded",
      },
      tooltip: {
        showTooltip: true,
        tooltipMessage: "Hello, let me help you find what you are looking for!",
        tooltipBackgroundColor: isDark ? "#2a2a2a" : "#fff8f0",
        tooltipTextColor: isDark ? "#f5f5f5" : "#2c2c2c",
        tooltipFontSize: 15,
      },
      customCSS: isDark ? ".n8n-chat-ui-bot-input-container { border: none !important; }" : "",
      chatWindow: {
        borderRadiusStyle: "rounded",
        avatarBorderRadius: 25,
        messageBorderRadius: 6,
        showTitle: true,
        title: "Seedboxes Docs AI",
        titleAvatarSrc: "https://www.svgrepo.com/show/339963/chat-bot.svg",
        avatarSize: 25,
        welcomeMessage:
          "Hello! Ask me a question and i will find the answer in our extended documentation!",
        backgroundColor: isDark ? "#1e1e1e" : "#ffffff",
        height: 900,
        width: 800,
        fontSize: 14,
        starterPromptFontSize: 15,
        renderHTML: true,
        clearChatOnReload: false,
        showScrollbar: false,
        botMessage: {
          backgroundColor: isDark ? "#352e25" : "#fef5e7",
          textColor: isDark ? "#e6c29f" : "#1e1e1e",
          showAvatar: true,
          avatarSrc: "https://www.svgrepo.com/show/190341/chat-conversation.svg",
          showCopyToClipboardIcon: true,
        },
        userMessage: {
          backgroundColor: isDark ? "#2f2f2f" : "#fdfdfd",
          textColor: isDark ? "#f0f0f0" : "#2c2c2c",
          showAvatar: true,
          avatarSrc: "https://www.svgrepo.com/show/190355/chat-conversation.svg",
        },
        textInput: {
          placeholder: "Type your query",
          backgroundColor: isDark ? "#2b2b2b" : "#ffffff",
          textColor: isDark ? "#cccccc" : "#2c2c2c",
          sendButtonColor: isDark ? "#f6bb42" : "#f6bb42",
          maxChars: 500,
          maxCharsWarningMessage:
            "You exceeded the characters limit. Please input less than 50 characters.",
          autoFocus: false,
          borderRadius: 6,
          sendButtonBorderRadius: 50,
        },
        uploadsConfig: {
          enabled: true,
          acceptFileTypes: ["png", "jpeg", "jpg", "txt"],
          maxSizeInMB: 5,
          maxFiles: 1,
        },
        voiceInputConfig: {
          enabled: true,
          maxRecordingTime: 15,
          recordingNotSupportedMessage:
            "To record audio, use modern browsers like Chrome or Firefox that support audio recording",
        },
        footer: {
            company: "Seedboxes.cc",
            companyLink: "https://www.seedboxes.cc",
            text: "Powered by",
            textColor: isDark ? "#ffffff" : "#2c2c2c",
        },
      },
    };
  };

  const hardRemoveExistingWidget = () => {
    const selectors = [
      "#n8nchatui-root",
      "[data-n8nchatui-root]",
      "iframe[src*='n8nchatui']",
      "div[id*='n8nchat']",
    ];
    selectors.forEach((sel) =>
      document.querySelectorAll(sel).forEach((el) => el.remove())
    );
  };

  const initChat = async (mode) => {
    const theme = buildTheme(mode);

    if (!ChatbotRef.current) {
      const mod = Chatbot;
      ChatbotRef.current = mod.default || mod;
    }

    // Prefer official destroy/update if available
    if (window.n8nChatUI?.destroy) {
      try {
        window.n8nChatUI.destroy();
      } catch {}
    } else {
      hardRemoveExistingWidget();
    }

    ChatbotRef.current.init({
      n8nChatUrl:
        "https://n8n.rapiddot.com/webhook/df5359c0-5a3e-43e8-8f66-409858dc3988/chat",
      metadata: {},
      theme,
      onReady: (api) => {
        window.n8nChatUI = api;
      },
    });
  };

  const getHtmlMode = () =>
    document.documentElement.getAttribute("data-theme") === "dark"
      ? "dark"
      : "light";

  useEffect(() => {
    if (typeof window === "undefined") return;

    // init with current mode
    const initialMode = getHtmlMode();
    currentModeRef.current = initialMode;
    initChat(initialMode);

    // watch for theme changes
    observerRef.current = new MutationObserver((mutations) => {
      for (const m of mutations) {
        if (
          m.type === "attributes" &&
          m.attributeName === "data-theme"
        ) {
          const newMode = getHtmlMode();
          if (newMode !== currentModeRef.current) {
            currentModeRef.current = newMode;
            initChat(newMode);
          }
        }
      }
    });
    observerRef.current.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ["data-theme"],
    });

    return () => {
      observerRef.current?.disconnect();
      if (window.n8nChatUI?.destroy) {
        try {
          window.n8nChatUI.destroy();
        } catch {}
      } else {
        hardRemoveExistingWidget();
      }
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return <>{children}</>;
}
