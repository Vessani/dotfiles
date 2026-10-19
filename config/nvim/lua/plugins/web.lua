-- HTML/CSS puros: LSPs (instalados pelo mason) + parser treesitter de css
return {
  {
    "neovim/nvim-lspconfig",
    opts = {
      servers = {
        html = {},
        cssls = {},
        emmet_language_server = {}, -- ex: div.card>ul>li*3 e aceitar no autocomplete
      },
    },
  },
  {
    "nvim-treesitter/nvim-treesitter",
    opts = { ensure_installed = { "css" } },
  },
}
