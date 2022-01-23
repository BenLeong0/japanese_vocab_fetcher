(this["webpackJsonpreact-interface"]=this["webpackJsonpreact-interface"]||[]).push([[0],Array(19).concat([function(e,t,n){},function(e,t,n){},,,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){"use strict";n.r(t);var a=n(1),r=n.n(a),s=n(12),c=n.n(s),i=(n(19),n(2)),o=n(10),l=n.p+"static/media/icon_error.f3363445.svg",u=(n(20),n(0)),d=function(e){var t=e.children;return Object(u.jsxs)("div",{className:"error-message vertical-separation-large",children:[Object(u.jsx)("img",{src:l,alt:"error icon"}),t,Object(u.jsx)("img",{src:l,alt:"error icon"})]})},j=n(4),m=n.n(j),b=n(6),f=n(13),p=(n(23),function(){return Object(u.jsx)("div",{className:"loader vertical-separation-large"})}),h=n(7),v=n(8),x=function(){function e(){var t=this;Object(h.a)(this,e),this.extractWordsFromInput=function(e){return e.split(/\s+/).filter((function(e){return""!==e}))},this.capitaliseString=function(e){return e?"( ".includes(e[0])?e[0]+t.capitaliseString(e.slice(1)):e[0].toUpperCase()+e.slice(1):e},this.copyStringToClipboard=function(e){navigator.clipboard.writeText(e)}}return Object(v.a)(e,[{key:"doubleURIEncode",value:function(e){return encodeURI(encodeURI(e))}},{key:"addQueryParamsToUrl",value:function(e,t){var n=Object.entries(t).map((function(e){return e.join("=")})).join("&");return e+"?"+this.doubleURIEncode(n)}}]),e}(),O=function(){function e(){Object(h.a)(this,e),this.API_URL="https://7z39hjjfg1.execute-api.eu-west-2.amazonaws.com/dev",this.utilsService=void 0,this.utilsService=new x}return Object(v.a)(e,[{key:"makeGetRequest",value:function(){var e=Object(b.a)(m.a.mark((function e(t,n){var a,r,s,c;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=this.API_URL+t,r={headers:{"Content-Type":"application/json"},method:"GET"},"undefined"!==typeof n&&(a=this.utilsService.addQueryParamsToUrl(a,n)),e.next=6,fetch(a,r);case 6:if(404!==(s=e.sent).status){e.next=9;break}throw new Error("An error occurred: "+s.statusText);case 9:return e.next=11,s.json();case 11:return c=e.sent,e.abrupt("return",c);case 13:case"end":return e.stop()}}),e,this)})));return function(t,n){return e.apply(this,arguments)}}()}]),e}(),g=(n(24),function(e){var t=e.setWordList,n=e.setErrorOccurred,r=Object(o.b)(),s=Object(i.a)(r,2),c=s[0],l=s[1],d=new O,j=new x,h=Object(a.useState)(""),v=Object(i.a)(h,2),g=v[0],w=v[1],N=Object(a.useState)(!1),y=Object(i.a)(N,2),_=y[0],k=y[1],S=Object(a.useRef)((function(e){}));S.current=function(){var e=Object(b.a)(m.a.mark((function e(a){var r,s,c,i;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return k(!0),n(!1),l({words:r=a||g}),s=j.extractWordsFromInput(r),c={words:JSON.stringify(s)},e.prev=6,e.next=9,d.makeGetRequest("/words",c);case 9:i=e.sent,t(i),console.log(i),e.next=18;break;case 14:e.prev=14,e.t0=e.catch(6),n(!0),console.log(e.t0);case 18:return e.prev=18,k(!1),e.finish(18);case 21:case"end":return e.stop()}}),e,null,[[6,14,18,21]])})));return function(t){return e.apply(this,arguments)}}();var D=Object(a.useCallback)((function(e){"Enter"===e.key&&e.ctrlKey&&S.current()}),[]);Object(a.useEffect)((function(){return window.addEventListener("keydown",D),function(){window.removeEventListener("keydown",D)}}),[D]);var E=Object(a.useRef)((function(){}));E.current=function(){var e=c.get("words");null!==e&&""!==e&&(w(e),S.current(e))},Object(a.useEffect)((function(){E.current()}),[]);var C=Object(u.jsx)(f.a,{name:"main-input",className:"main-input",value:g,onChange:function(e){return w(e.target.value)}}),I=Object(u.jsx)("div",{className:"words-display vertical-separation-small",children:j.extractWordsFromInput(g).map((function(e,t){return Object(u.jsx)("div",{className:"word-display",children:e},t)}))}),F=Object(u.jsx)("button",{className:"button-primary vertical-separation-medium",type:"submit",onClick:function(e){return S.current()},children:"Submit"});return _?Object(u.jsx)(p,{}):Object(u.jsxs)(u.Fragment,{children:[C,I,F]})}),w=(n(25),function(e){var t=e.setWordList,n=Object(a.useState)(!1),r=Object(i.a)(n,2),s=r[0],c=r[1];return Object(u.jsxs)("div",{className:"input-page",children:[Object(u.jsx)(g,{setWordList:t,setErrorOccurred:c}),s&&Object(u.jsx)(d,{children:"An error occurred. Please try again"})]})}),N=n.p+"static/media/icon_plus.2cc3b49e.svg",y=n.p+"static/media/icon_minus.b9223dca.svg",_=(n(26),function(e){var t=e.currentDisplay,n=e.updateDisplay,a=e.maxDisplay,r=e.minDisplay,s=e.batchSize;return Object(u.jsxs)("div",{className:"expand-button-container flex-row unselectable",children:[t>r&&Object(u.jsx)("div",{className:"expand-button expand-button-decrease",onClick:function(){return n(Math.max(r,t-s))},children:Object(u.jsx)("img",{src:y,alt:"button to decrease the number of items displayed"})}),t<a&&Object(u.jsx)("div",{className:"expand-button expand-button-increase",onClick:function(){return n(Math.min(a,t+s))},children:Object(u.jsx)("img",{src:N,alt:"button to increase the number of items displayed"})})]})}),k=function(e){var t=e.rowsDisplay,n=e.updateRowsDisplay;return Object(u.jsx)(_,{updateDisplay:function(e){n(1===e)},minDisplay:0,maxDisplay:1,batchSize:1,currentDisplay:t?1:0})},S=n.p+"static/media/icon_play_button.7a4d59b8.svg",D=n.p+"static/media/icon_stop_button.00ad3332.svg",E=function(e){var t=e.audioData,n=Object(a.useState)(new Audio(t.url)),r=Object(i.a)(n,1)[0],s=Object(a.useState)(!1),c=Object(i.a)(s,2),o=c[0],l=c[1];return Object(a.useEffect)((function(){r.currentTime=0,o?r.play():r.pause()}),[o]),Object(a.useEffect)((function(){return r.addEventListener("ended",(function(){return l(!1)})),function(){r.removeEventListener("ended",(function(){return l(!1)}))}}),[]),Object(u.jsxs)("div",{className:"result-audio-row flex-row",children:[Object(u.jsx)("img",{src:o?D:S,alt:"audio player icon",className:"audio-player unselectable",onClick:function(){return l(!o)}}),Object(u.jsx)("div",{className:"result-audio-speaker",children:t.speaker}),Object(u.jsx)("div",{className:"result-audio-subtitle",children:t.subtitle||""})]})},C=function(e){var t=e.moduleTitle,n=e.audioData,r=Object(a.useState)(!1),s=Object(i.a)(r,2),c=s[0],o=s[1];return Object(u.jsxs)("div",{className:"result-audio-module vertical-separation-small",children:[Object(u.jsx)("div",{className:"audio-module-title",children:t}),n.filter((function(e,t){return function(e){return e<2||2===e&&3===n.length||!0===c}(t)})).map((function(e){return Object(u.jsx)(E,{audioData:e},e.speaker)})),n.length>3&&Object(u.jsx)(k,{rowsDisplay:c,updateRowsDisplay:o})]})},I=(n(27),function(e){var t=e.data,n=[{module:"Wanikani",audioData:t.wanikani.main_data.audio.map((function(e){return{url:e.url,speaker:e.metadata.voice_actor_name,subtitle:e.metadata.voice_description}}))},{module:"Forvo",audioData:t.forvo.main_data.audio.map((function(e){return{url:e.url,speaker:e.username,subtitle:null}}))},{module:"JapanesePod101",audioData:t.japanesepod.main_data.audio.map((function(e){return{url:e.url,speaker:e.writing,subtitle:e.reading}}))}];return n.some((function(e){return e.audioData.length>0}))?Object(u.jsxs)("div",{className:"result-audio",children:[Object(u.jsx)("div",{className:"left-col-title",children:"Audio"}),n.filter((function(e){return e.audioData.length>0})).map((function(e){var t=e.module,n=e.audioData;return Object(u.jsx)(C,{moduleTitle:t,audioData:n},t)}))]}):Object(u.jsx)(u.Fragment,{})}),F=function(e){var t=e.ordinality,n=e.sense,a=new x,r=t+". "+n.english_definitions.map(a.capitaliseString).join(" ; ");return Object(u.jsxs)("div",{className:"result-definition-sense flex-col",children:[Object(u.jsx)("div",{className:"sense-part-of-speech",children:function(){var e=n.parts_of_speech.join("\u30fb");return n.tags.length>0&&(e+=" ("+n.tags.join(", ")+")"),e}()}),Object(u.jsx)("div",{className:"sense-english-definition",children:r})]})},z=function(e){var t=e.definitionData,n=function(e){return(e.word||e.reading||"")+(e.word&&e.reading?"\u3010".concat(e.reading,"\u3011"):"")},a=t.japanese.slice(1);return Object(u.jsxs)("div",{className:"result-definition flex-col",children:[Object(u.jsx)("div",{className:"result-definition-title mplus",children:n(t.japanese[0])}),Object(u.jsxs)("div",{className:"result-definition-senses-container flex-col",children:[t.senses.map((function(e,t){return Object(u.jsx)(F,{ordinality:t+1,sense:e},t)})),a.length>0&&Object(u.jsxs)("div",{className:"result-definition-other-forms flex-col",children:[Object(u.jsx)("div",{className:"result-other-forms-title",children:"Other forms"}),Object(u.jsx)("div",{className:"result-other-forms-words mplus",children:a.map(n).join("\u3001")})]})]})]})},T=(n(28),function(e){var t=e.data;return Object(u.jsx)("div",{className:"result-definitions-container flex-col",children:t.jisho.main_data.results.map((function(e){return Object(u.jsx)(z,{definitionData:e},e.slug)}))})}),L=function(e){var t=e.title,n=e.readings,a=new x;return Object(u.jsxs)("div",{className:"readings-row",children:[Object(u.jsxs)("div",{className:"readings-row-left",children:[t,":"]}),Object(u.jsx)("div",{className:"readings-row-right",children:n.map((function(e,t){return Object(u.jsx)("div",{className:"reading unselectable",onClick:function(){!function(e){a.copyStringToClipboard(e)}(e)},title:"Copy to clipboard",children:e},t)}))})]})},R=(n(29),function(e){var t=e.data,n=[{title:"OJAD",readings:t.ojad.main_data.accent},{title:"Wadoku",readings:t.wadoku.main_data.accent},{title:"Suzuki",readings:t.suzuki.main_data.accent}],a=function(e){return e.readings.length>0};return n.some(a)?Object(u.jsxs)("div",{className:"result-readings",children:[Object(u.jsx)("div",{className:"left-col-title",children:"Readings"}),n.filter(a).map((function(e){var t=e.title,n=e.readings;return Object(u.jsx)(L,{title:t,readings:n},t)}))]}):Object(u.jsx)(u.Fragment,{})}),W=function(e){var t=e.relatedWord,n=t.slug,a=t.japanese,r="https://jisho.org/word/".concat(n);return Object(u.jsx)("div",{className:"related-word",onClick:function(){return window.open(r,"_blank")},children:a[0].word||a[0].reading})},P=(n(30),function(e){var t=e.data;return t.jisho.main_data.extra.length>0?Object(u.jsxs)("div",{className:"result-related-words vertical-separation-small",children:[Object(u.jsx)("div",{className:"left-col-title",children:"Related words"}),Object(u.jsx)("div",{className:"related-words-container flex-row",children:t.jisho.main_data.extra.map((function(e){return Object(u.jsx)(W,{relatedWord:e},e.slug)}))})]}):Object(u.jsx)(u.Fragment,{})}),A=n(9),U=n(14);function M(){return(M=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var n=arguments[t];for(var a in n)Object.prototype.hasOwnProperty.call(n,a)&&(e[a]=n[a])}return e}).apply(this,arguments)}function J(e,t){if(null==e)return{};var n,a,r=function(e,t){if(null==e)return{};var n,a,r={},s=Object.keys(e);for(a=0;a<s.length;a++)n=s[a],t.indexOf(n)>=0||(r[n]=e[n]);return r}(e,t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(a=0;a<s.length;a++)n=s[a],t.indexOf(n)>=0||Object.prototype.propertyIsEnumerable.call(e,n)&&(r[n]=e[n])}return r}var B=a.createElement("path",{d:"M10 8h-2v2h-2v-4h4v2zm8 16v-2h-6v2h6zm2-16h2v2h2v-4h-4v2zm2 12v2h-2v2h4v-4h-2zm-12 2h-2v-2h-2v4h4v-2zm14-10h-2v6h2v-6zm-16 6v-6h-2v4h-4v-14h14v4h-4v2h6v-8h-18v18h8z"});function G(e,t){var n=e.title,r=e.titleId,s=J(e,["title","titleId"]);return a.createElement("svg",M({xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",ref:t,"aria-labelledby":r},s),n?a.createElement("title",{id:r},n):null,B)}var q=a.forwardRef(G),Q=(n.p,function(e){var t=e.sentence,n=e.source,a=new x;return Object(u.jsxs)(u.Fragment,{children:[Object(u.jsxs)("div",{className:"result-sentence flex-col hide-mobile",children:[Object(u.jsxs)("div",{className:"result-sentence-top flex-row",children:[Object(u.jsx)("div",{className:"result-sentence-ja",children:t.ja}),Object(u.jsxs)("div",{className:"result-sentence-extra flex-row",children:[Object(u.jsx)("div",{className:"result-sentence-source",children:"- ".concat(n)}),Object(u.jsx)(q,{className:"result-sentence-copy",onClick:function(){a.copyStringToClipboard(t.ja+"\t"+t.en)}})]})]}),Object(u.jsx)("div",{className:"result-sentence-en",children:t.en})]}),Object(u.jsxs)("div",{className:"result-sentence flex-col show-mobile",children:[Object(u.jsx)("div",{className:"result-sentence-ja",children:t.ja}),Object(u.jsx)("div",{className:"result-sentence-en",children:t.en}),Object(u.jsx)("div",{className:"result-sentence-source",children:"- ".concat(n)})]})]})}),K=(n(31),function(e){for(var t=Math.max.apply(Math,Object(U.a)(e.map((function(e){return e.length})))),n=[],a=0;a<t;a++){var r,s=Object(A.a)(e);try{for(s.s();!(r=s.n()).done;){var c=r.value;a<c.length&&n.push(c[a])}}catch(i){s.e(i)}finally{s.f()}}return n}),V=function(e){var t=e.data,n=t.wanikani.main_data.sentences.map((function(e){return{sentence:e,source:"Wanikani"}})),r=t.tangorin.main_data.sentences.map((function(e){return{sentence:e,source:"Tangorin"}})),s=K([n,r]),c=s.length,o=Math.min(s.length,4),l=Object(a.useState)(o),d=Object(i.a)(l,2),j=d[0],m=d[1];return s.length>0?Object(u.jsxs)("div",{className:"result-sentences flex-col",children:[Object(u.jsx)("div",{className:"right-col-title",children:"Context Sentences"}),Object(u.jsxs)("div",{className:"result-sentences-container flex-col",children:[s.filter((function(e,t){return t+1<=j})).map((function(e){var t=e.sentence,n=e.source;return Object(u.jsx)(Q,{sentence:t,source:n},t.ja)})),Object(u.jsx)(_,{currentDisplay:j,updateDisplay:m,maxDisplay:c,minDisplay:o,batchSize:4})]})]}):Object(u.jsx)(u.Fragment,{})},H=function(e){var t=e.tag,n="wanikani"===t.slice(0,8)?"wanikani level ".concat(t.slice(8)):t.toLowerCase().replace("-"," ");return Object(u.jsx)("div",{className:"result-tag",children:n})},X=(n(32),function(e){var t=e.jisho.main_data.results.map((function(e){return[e.jlpt,e.tags]})).flat(2);return e.jisho.main_data.results.some((function(e){return e.is_common}))&&t.push("common word"),t}),Y=function(e){var t=e.data,n=X(t);return n.length>0?Object(u.jsx)("div",{className:"result-tags-container flex-row",children:n.map((function(e){return Object(u.jsx)(H,{tag:e},e)}))}):Object(u.jsx)(u.Fragment,{})},Z=n.p+"static/media/icon_copy.e4e97c1f.svg",$=(n(33),function(e){var t=e.children,n=e.isExpanded,a=e.toggleIsExpanded,r=e.copyString,s=new x;return Object(u.jsxs)("div",{className:"result-title flex-row space-between",children:[Object(u.jsx)("div",{className:"result-title-text mplus",children:t}),Object(u.jsxs)("div",{className:"result-title-buttons flex-col space-between",children:[Object(u.jsx)("img",{className:"result-title-copy unselectable",src:Z,alt:"button to copy sample row to clipboard",onClick:function(){s.copyStringToClipboard(r)}}),Object(u.jsx)("div",{className:"result-title-collapser unselectable",onClick:a,children:n?"collapse":"expand"})]})]})}),ee=n.p+"static/media/icon_chevron_up.0c1b14a0.svg",te=n.p+"static/media/icon_chevron_down.fee13e32.svg",ne=(n(34),function(e){var t=e.isExpanded,n=e.toggleIsExpanded,a=t?ee:te;return Object(u.jsx)("div",{className:"result-toggle-bar unselectable",onClick:n,children:Object(u.jsx)("img",{src:a,alt:"chevron to expand or collapse the result"})})}),ae=(n(35),function(e){var t=e.data,n=new x,r=Object(a.useState)(!0),s=Object(i.a)(r,2),c=s[0],o=s[1],l=function(){return o(!c)},d=function(){return t.wanikani.main_data.sentences.length>0?t.wanikani.main_data.sentences[0]:t.tangorin.main_data.sentences.length>0?t.tangorin.main_data.sentences[0]:{en:"",ja:""}},j=[function(){var e=function(e){return e.parts_of_speech.includes("Suru verb")};return t.jisho.main_data.results.some((function(t){return t.senses.some(e)}))?t.word+"\uff08\u3059\u308b\uff09":t.word}(),t.ojad.main_data.accent.length>0?t.ojad.main_data.accent[0]:t.wadoku.main_data.accent.length>0?t.wadoku.main_data.accent[0]:t.suzuki.main_data.accent.length>0?t.suzuki.main_data.accent[0]:"",0===t.jisho.main_data.results.length?"":t.jisho.main_data.results.map((function(e){return e.senses})).flat(2).map((function(e){return e.english_definitions.slice(0,2)})).map((function(e){return e.map((function(e){return n.capitaliseString(e)}))})).map((function(e){return e.join(" ; ")})).join("  /  "),d().ja,d().en].join("\t");return Object(u.jsxs)("div",{className:"result-block flex-col",children:[Object(u.jsx)($,{isExpanded:c,toggleIsExpanded:l,copyString:j,children:t.word}),c&&Object(u.jsxs)(u.Fragment,{children:[Object(u.jsxs)("div",{className:"flex-row hide-mobile",children:[Object(u.jsxs)("div",{className:"result-left-col flex-col",children:[Object(u.jsx)(R,{data:t}),Object(u.jsx)(Y,{data:t}),Object(u.jsx)(I,{data:t}),Object(u.jsx)(P,{data:t})]}),Object(u.jsx)("div",{className:"result-col-separator"}),Object(u.jsxs)("div",{className:"result-right-col flex-col",children:[Object(u.jsx)(T,{data:t}),Object(u.jsx)(V,{data:t})]})]}),Object(u.jsxs)("div",{className:"flex-col show-mobile",children:[Object(u.jsx)(R,{data:t}),Object(u.jsx)(Y,{data:t}),Object(u.jsx)(T,{data:t}),Object(u.jsx)(I,{data:t}),Object(u.jsx)(V,{data:t}),Object(u.jsx)(P,{data:t})]})]}),Object(u.jsx)(ne,{isExpanded:c,toggleIsExpanded:l})]})}),re=(n(36),function(e){var t=e.wordList;return Object(u.jsx)("div",{className:"results-list",children:t.map((function(e){return Object(u.jsx)(ae,{data:e},e.word)}))})});n(37);var se=function(){var e=Object(a.useState)([]),t=Object(i.a)(e,2),n=t[0],r=t[1];return Object(u.jsx)(o.a,{children:Object(u.jsx)("div",{className:"App",children:Object(u.jsxs)("div",{className:"width-container",children:[Object(u.jsx)("p",{className:"app-header",children:"Japanese Vocab Fetcher"}),Object(u.jsx)(w,{setWordList:r}),Object(u.jsx)(re,{wordList:n})]})})})},ce=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,39)).then((function(t){var n=t.getCLS,a=t.getFID,r=t.getFCP,s=t.getLCP,c=t.getTTFB;n(e),a(e),r(e),s(e),c(e)}))};c.a.render(Object(u.jsx)(r.a.StrictMode,{children:Object(u.jsx)(se,{})}),document.getElementById("root")),ce()}]),[[38,1,2]]]);
//# sourceMappingURL=main.8073fba6.chunk.js.map