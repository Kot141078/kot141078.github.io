-- Rendering only: keep source text but permit long technical identifiers to wrap.
function Code(el)
  if FORMAT:match('latex') then
    if #el.text > 24 and not el.text:match('[{}\\\n]') then
      return pandoc.RawInline('latex', '\\nolinkurl{' .. el.text .. '}')
    end
    local text = el.text:gsub('\\', '@@BS@@'):gsub('([%%#$&_{}])', '\\%1')
    text = text:gsub('@@BS@@', '\\textbackslash{}')
    text = text:gsub('\\_', '\\_\\allowbreak{}')
    return pandoc.RawInline('latex', '\\texttt{' .. text .. '}')
  end
end
function Header(el)
  if FORMAT:match('latex') and el.level == 1 then
    local text = pandoc.utils.stringify(el.content)
    if text:match('^04_C_CONTINUITY_METRIC') then
      el.content = pandoc.Inlines{pandoc.Str('04 — Continuity Metric and Equivalence Semantics (predecessor v0.1.2)')}
    end
  end
  return el
end
