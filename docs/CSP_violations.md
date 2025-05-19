# CSP violations

unsafe-inline violations

| **source**    | **line**                                                         | **hash**                                              | **N** |
|---------------|------------------------------------------------------------------|-------------------------------------------------------|-------|
|               | Golem injected js custom messagehandlers                         | 'sha256-5MbwhvReB6ydVeF1RSceiLsOoPftOKOVzlxxWHtfWlM=' |       |
|               | shinyjs injected js custom messagehandlers (in use)              | 'sha256-1TPYfIdHccePeJW/uvh6P6ubWSQrZYBs6o34RcqX5XE=' |       |
|               | shinyjs.debug = false;                                           | 'sha256-DiOXoTwxysY/p6mCaMFek/cgVVW2xis7beHYjl9R8Ws=' |       |
|               | bslib.Card.initializeAllCards()                                  | 'sha256-uu+K0xL4psk7EtdJAaHm0ZepO3JyoN1gGtITOrTV2T8=' | 18    |
|               | bslib.Sidebar.initCollapsibleAll                                 | 'sha256-AEI89C+q4+rK1PjOGaxznR7D+lBg+RgqTsMtW1nPXOE=' | 11    |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-JDYsFFqB4eL9lRhcQwDSWVr7LK3Z8VgMLdzpW8GbIIQ=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-3iXHrfSd4xzI1YyrooF0jG4OVwGiSAoU1+WdYwEwYZk=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-qj08NPX5C0V2ohqUsFBIKItiCRMe5J53oBryTx6tp3g=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-qEVbr7EsNKFDj8cJG6hOzCzP0Qz+KJ+0FASnh4+rq8w=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-ALr4xiM6d06xwYlcW1/nw0xxUI/Vufi1Zrw6HRPkPRI=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-Ss5DDvFdpRhDDq0MHIeNCEmbmmDmrmKXQSCCtmgmERY=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-rMfkFFWoB2W1/Zx+4bgHim0WC7vKRVrq6FTeZclH1Z4=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-p4CAZ0vtCH7uouzJXpuPx7UAq1Sl1Q7xyYeLgde7Cz8=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-Kd8QDM9jqFmpd0R+KkPsGIWl+NBtG7iKlSNXmVRGPss=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-G4idrOlCTf0E/ZSfMhef+6B2K+RZkYUUw2mKdmP4LBE=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-8qpfNjLKRiQaMsj2vqPFBZ/jbtoTLNWUmB0ohw32BEE=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-nroMpWKYJcftREE92iVGOgvIyBB5T3K3sOuTseQx7HQ=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-2V3aKpoKxtdPKkcwdLnWE7WkOoOx28hZDCR9naHiKzs=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-wyylxU+1l4l1p9f2aci9QKCs+443wJ6S1hJvEZ9TheE=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-q+IXUCsEBhRv4DoV762VlqMP674accpwNtHLUh6w4Jk=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-2pYj29iyEVNJ3ObKmJpTaCPjFgYo1R0EVxG5f3DQ/bg=' | 1     |
| jquery.js:133 | doc.head.appendChild( script ).parentNode.removeChild( script ); | 'sha256-q+IXUCsEBhRv4DoV762VlqMP674accpwNtHLUh6w4Jk=' | 1     |

unsafe-eval violations:

+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| source                       | script                                                                                                                                                                                                                                                                                         |
+==============================+================================================================================================================================================================================================================================================================================================+
| bind.ts:343                  | setTimeout(sendImageSizeFns.regular, 0);\                                                                                                                                                                                                                                                      |
|                              | setTimeout(sendOutputHiddenState, 0);                                                                                                                                                                                                                                                          |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| index.ts:152                 | func = new Function("with (this) {\\n try {\\n return (".concat(expr, ");\\n } catch (e) {\\n console.error('Error evaluating expression: ").concat(exprEscaped, "');\\n throw e;\\n }\\n }"));                                                                                                |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| shinyjs-default-funcs.js:701 | runjs : function (params) { var defaultParams = { code : null  }  params = shinyjs.getParams(params, defaultParams);  eval(params.code);  },                                                                                                                                                   |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| htmlwidgets.js:252           | function tryEval(code) { var result = null; try { result = eval("(" + code + ")"); } catch(error) {  if (!(error instanceof SyntaxError)) { throw error;  } try { \|result = eval(code);  } catch(e) {  if (e instanceof SyntaxError) { throw error;  } else { throw e;  } }  return result; } |
+------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
