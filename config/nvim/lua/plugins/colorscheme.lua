return {
  {
    "scottmckendry/cyberdream.nvim",
    lazy = false,
    priority = 1000,
    opts = {
      variant = "default",
      transparent = true,
      italic_comments = true,
      borderless_pickers = false,
      terminal_colors = true,
      extensions = {
        blinkcmp = true,
        gitsigns = true,
        lazy = true,
        mini = true,
        noice = true,
        snacks = true,
        trouble = true,
        whichkey = true,
      },
    },
  },
  -- mantém o catppuccin instalado, caso queira voltar: :colorscheme catppuccin
  { "catppuccin/nvim", name = "catppuccin", lazy = true, opts = { transparent_background = true } },
  {
    "nvim-lualine/lualine.nvim",
    opts = function(_, opts)
      opts.options = opts.options or {}
      opts.options.theme = "auto"
    end,
  },
}
