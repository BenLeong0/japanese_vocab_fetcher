(this["webpackJsonpreact-interface"]=this["webpackJsonpreact-interface"]||[]).push([[0],[,,,,,,,,,,,,,,function(e,t,n){},function(e,t,n){},,,function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){},function(e,t,n){"use strict";n.r(t);var a=n(1),s=n.n(a),r=n(8),c=n.n(r),i=(n(14),n(2)),o=n.p+"static/media/icon_error.f3363445.svg",l=(n(15),n(0)),d=function(e){var t=e.children;return Object(l.jsxs)("div",{className:"error-message vertical-separation-large",children:[Object(l.jsx)("img",{src:o,alt:"error icon"}),t,Object(l.jsx)("img",{src:o,alt:"error icon"})]})},u=n(3),j=n.n(u),f=n(4),b=n(9),m=(n(18),function(){return Object(l.jsx)("div",{className:"loader vertical-separation-large"})}),x=n(5),v=n(6),O=function(){function e(){Object(x.a)(this,e),this.extractWordsFromInput=function(e){return e.split(/\s+/).filter((function(e){return""!==e}))}}return Object(v.a)(e,[{key:"addQueryParamsToUrl",value:function(e,t){return e+"?"+Object.entries(t).map((function(e){return e.join("=")})).join("&")}}]),e}(),p=function(){function e(){Object(x.a)(this,e),this.API_URL="http://3.8.95.26:5000",this.utilsService=void 0,this.utilsService=new O}return Object(v.a)(e,[{key:"makeGetRequest",value:function(){var e=Object(f.a)(j.a.mark((function e(t,n){var a,s,r,c;return j.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return a=this.API_URL+t,s={method:"GET",headers:{"Content-Type":"application/json",Referer:"https://benleong0.github.io/japanese_vocab_fetcher/"}},"undefined"!==typeof n&&(a=this.utilsService.addQueryParamsToUrl(a,n)),e.next=6,fetch(a,s);case 6:if(404!==(r=e.sent).status){e.next=9;break}throw new Error("An error occurred: "+r.statusText);case 9:return e.next=11,r.json();case 11:return c=e.sent,e.abrupt("return",c);case 13:case"end":return e.stop()}}),e,this)})));return function(t,n){return e.apply(this,arguments)}}()}]),e}(),h=(n(19),function(e){var t=e.setWordList,n=e.setErrorOccurred,s=new p,r=new O,c=Object(a.useState)(""),o=Object(i.a)(c,2),d=o[0],u=o[1],x=Object(a.useState)(!1),v=Object(i.a)(x,2),h=v[0],g=v[1],N=Object(a.useRef)((function(){}));N.current=Object(f.a)(j.a.mark((function e(){var a,c,i;return j.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return g(!0),n(!1),a=r.extractWordsFromInput(d),c={words:JSON.stringify(a)},e.prev=4,e.next=7,s.makeGetRequest("/words",c);case 7:i=e.sent,t(i),console.log(i),e.next=16;break;case 12:e.prev=12,e.t0=e.catch(4),n(!0),console.log(e.t0);case 16:return e.prev=16,g(!1),e.finish(16);case 19:case"end":return e.stop()}}),e,null,[[4,12,16,19]])})));var w=Object(a.useCallback)((function(e){"Enter"===e.key&&e.ctrlKey&&N.current()}),[]);Object(a.useEffect)((function(){return window.addEventListener("keydown",w),function(){window.removeEventListener("keydown",w)}}),[w]);var k=Object(l.jsx)(b.a,{name:"main-input",className:"main-input",value:d,onChange:function(e){return u(e.target.value)}}),_=Object(l.jsx)("div",{className:"words-display vertical-separation-small",children:r.extractWordsFromInput(d).map((function(e,t){return Object(l.jsx)("div",{className:"word-display",children:e},t)}))}),y=Object(l.jsx)("button",{className:"button-primary vertical-separation-medium",type:"submit",onClick:function(e){return N.current()},children:"Submit"});return h?Object(l.jsx)(m,{}):Object(l.jsxs)(l.Fragment,{children:[k,_,y]})}),g=(n(20),function(e){var t=e.setWordList,n=Object(a.useState)(!1),s=Object(i.a)(n,2),r=s[0],c=s[1];return Object(l.jsxs)("div",{className:"input-page",children:[Object(l.jsx)(h,{setWordList:t,setErrorOccurred:c}),r?Object(l.jsx)(d,{children:"An error occurred. Please try again"}):Object(l.jsx)(l.Fragment,{})]})}),N=(n(21),n.p+"static/media/icon_play_button.7a4d59b8.svg"),w=n.p+"static/media/icon_stop_button.00ad3332.svg",k=function(e){var t=e.rowIndex,n=e.audioData,s=e.isExpanded,r=Object(a.useState)(new Audio(n.url)),c=Object(i.a)(r,1)[0],o=Object(a.useState)(!1),d=Object(i.a)(o,2),u=d[0],j=d[1];return Object(a.useEffect)((function(){c.currentTime=0,u?c.play():c.pause()}),[u]),Object(a.useEffect)((function(){return c.addEventListener("ended",(function(){return j(!1)})),function(){c.removeEventListener("ended",(function(){return j(!1)}))}}),[]),s||t<2?Object(l.jsxs)("div",{className:"result-audio-row flex-row",children:[Object(l.jsx)("img",{src:u?w:N,alt:"audio player icon",className:"audio-player",onClick:function(){return j(!u)}}),Object(l.jsx)("div",{className:"result-audio-speaker",children:n.speaker}),Object(l.jsx)("div",{className:"result-audio-subtitle",children:n.subtitle||""})]}):Object(l.jsx)(l.Fragment,{})},_=n.p+"static/media/icon_plus.2cc3b49e.svg",y=n.p+"static/media/icon_minus.b9223dca.svg",E=function(e){var t=e.moduleTitle,n=e.audioData,s=Object(a.useState)(!1),r=Object(i.a)(s,2),c=r[0],o=r[1];return Object(l.jsxs)("div",{className:"result-audio-module vertical-separation-small",children:[Object(l.jsx)("div",{className:"audio-module-title",children:t}),n.map((function(e,t){return Object(l.jsx)(k,{rowIndex:t,audioData:e,isExpanded:c},e.speaker)})),n.length>2&&Object(l.jsx)("div",{className:"audio-expand-toggle",onClick:function(){return o(!c)},children:Object(l.jsx)("img",{src:c?y:_,alt:"button to toggle expanded list of audio files"})})]})},S=function(e){var t=e.data,n=t.wanikani.main_data.audio.map((function(e){return{url:e.url,speaker:e.metadata.voice_actor_name,subtitle:e.metadata.voice_description}})),a=t.forvo.main_data.audio.map((function(e){return{url:e.url,speaker:e.username,subtitle:null}}));return Object(l.jsxs)("div",{className:"result-audio",children:[Object(l.jsx)("div",{className:"left-col-title",children:"Audio"}),n.length>0&&Object(l.jsx)(E,{moduleTitle:"Wanikani",audioData:n}),a.length>0&&Object(l.jsx)(E,{moduleTitle:"Forvo",audioData:a}),Object(l.jsx)(E,{moduleTitle:"JapanesePod101",audioData:[{url:"https://audiostock-public-files.s3.ap-northeast-1.amazonaws.com/sample-files/demo_34d52dc1ec6ba4736f37c24458a2a7812e9b56f6.mp3",speaker:"Coming soon!",subtitle:null}]})]})},C=function(e){var t=e.ordinality,n=e.sense,a=t+". "+n.english_definitions.join("; ");return Object(l.jsxs)("div",{className:"result-definition-sense flex-col",children:[Object(l.jsx)("div",{className:"sense-part-of-speech",children:function(){var e=n.parts_of_speech.join(", ");return n.tags.length>0&&(e+=" ("+n.tags.join(", ")+")"),e}()}),Object(l.jsx)("div",{className:"sense-english-definition",children:a})]})},L=function(e){var t=e.definitionData,n=function(e){return(e.word||e.reading||"")+(e.word&&e.reading&&"\u3010".concat(e.reading,"\u3011"))},a=t.japanese.slice(1);return Object(l.jsxs)("div",{className:"result-definition flex-col",children:[Object(l.jsx)("div",{className:"result-definition-title",children:n(t.japanese[0])}),Object(l.jsxs)("div",{className:"result-definition-senses-container flex-col",children:[t.senses.map((function(e,t){return Object(l.jsx)(C,{ordinality:t+1,sense:e},t)})),a.length>0&&Object(l.jsxs)("div",{className:"result-definition-other-forms flex-col",children:[Object(l.jsx)("div",{className:"result-other-forms-title",children:"Other forms"}),Object(l.jsx)("div",{className:"result-other-forms-words",children:a.map(n).join("\u3001")})]})]})]})},I=(n(22),function(e){var t=e.data;return Object(l.jsx)("div",{className:"result-definitions-container flex-col",children:t.jisho.main_data.results.map((function(e){return Object(l.jsx)(L,{definitionData:e},e.slug)}))})}),F=(n(23),function(e){var t=e.title,n=e.readings;return Object(l.jsxs)("div",{className:"readings-row",children:[Object(l.jsxs)("div",{className:"readings-row-left",children:[t,":"]}),Object(l.jsx)("div",{className:"readings-row-right",children:n.map((function(e,t){return Object(l.jsx)("div",{className:"reading",children:e},t)}))})]})}),T=function(e){var t=e.data,n=[{title:"OJAD",readings:t.ojad.main_data.accent},{title:"Wadoku",readings:t.wadoku.main_data.accent},{title:"Suzuki",readings:t.suzuki.main_data.accent}];return Object(l.jsxs)("div",{className:"result-readings",children:[Object(l.jsx)("div",{className:"left-col-title",children:"Readings"}),n.map((function(e){var t=e.title,n=e.readings;return Object(l.jsx)(F,{title:t,readings:n},t)}))]})},W=function(e){var t=e.relatedWord,n=t.slug,a=t.japanese,s="https://jisho.org/word/".concat(n);return Object(l.jsx)("div",{className:"related-word",onClick:function(){return window.open(s,"_blank")},children:a[0].word||a[0].reading})},D=(n(24),function(e){var t=e.data;return Object(l.jsxs)("div",{className:"result-related-words vertical-separation-small",children:[Object(l.jsx)("div",{className:"left-col-title",children:"Related words"}),Object(l.jsx)("div",{className:"related-words-container flex-row",children:t.jisho.main_data.extra.map((function(e){return Object(l.jsx)(W,{relatedWord:e},e.slug)}))})]})}),A=function(e){var t=e.sentence,n=e.source;return Object(l.jsxs)("div",{className:"result-sentence flex-col",children:[Object(l.jsxs)("div",{className:"result-sentence-top flex-row",children:[Object(l.jsx)("div",{className:"result-sentence-ja",children:t.ja}),Object(l.jsx)("div",{className:"result-sentence-source",children:"- ".concat(n)})]}),Object(l.jsx)("div",{className:"result-sentence-en",children:t.en})]})},P=(n(25),function(e){var t=e.data;return Object(l.jsxs)("div",{className:"result-sentences flex-col",children:[Object(l.jsx)("div",{className:"right-col-title",children:"Context Sentences"}),Object(l.jsx)("div",{className:"result-sentences-container flex-col",children:t.wanikani.main_data.sentences.map((function(e){return Object(l.jsx)(A,{sentence:e,source:"Wanikani"},e.ja)}))})]})}),R=function(e){var t=e.tag,n="wanikani"===t.slice(0,8)?"wanikani level ".concat(t.slice(8)):t.toLowerCase().replace("-"," ");return Object(l.jsx)("div",{className:"result-tag",children:n})},J=(n(26),function(e){var t=e.jisho.main_data.results.map((function(e){return[e.jlpt,e.tags]})).flat(2);return e.jisho.main_data.results.some((function(e){return e.is_common}))&&t.push("common word"),t}),U=function(e){var t=e.data,n=J(t);return Object(l.jsx)("div",{className:"result-tags-container flex-row",children:n.map((function(e){return Object(l.jsx)(R,{tag:e},e)}))})},z=(n(27),function(e){var t=e.children,n=e.isExpanded,a=e.toggleIsExpanded;return Object(l.jsxs)("div",{className:"result-title",children:[Object(l.jsx)("div",{className:"result-title-text",children:t}),Object(l.jsx)("div",{className:"title-collapser",onClick:a,children:n?"collapse":"expand"})]})}),G=n.p+"static/media/icon_chevron_up.0c1b14a0.svg",q=n.p+"static/media/icon_chevron_down.fee13e32.svg",B=(n(28),function(e){var t=e.isExpanded,n=e.toggleIsExpanded,a=t?G:q;return Object(l.jsx)("div",{className:"result-toggle-bar",onClick:n,children:Object(l.jsx)("img",{src:a,alt:"chevron to expand or collapse the result"})})}),Q=(n(29),function(e){var t=e.data,n=Object(a.useState)(!0),s=Object(i.a)(n,2),r=s[0],c=s[1],o=function(){return c(!r)};return Object(l.jsxs)("div",{className:"result-block flex-col",children:[Object(l.jsx)(z,{isExpanded:r,toggleIsExpanded:o,children:t.word}),r&&Object(l.jsxs)("div",{className:"flex-row",children:[Object(l.jsxs)("div",{className:"result-left-col flex-col",children:[Object(l.jsx)(T,{data:t}),Object(l.jsx)(U,{data:t}),Object(l.jsx)(S,{data:t}),Object(l.jsx)(D,{data:t})]}),Object(l.jsx)("div",{className:"result-col-separator"}),Object(l.jsxs)("div",{className:"result-right-col flex-col",children:[Object(l.jsx)(I,{data:t}),Object(l.jsx)(P,{data:t})]})]}),Object(l.jsx)(B,{isExpanded:r,toggleIsExpanded:o})]})}),K=(n(30),function(e){var t=e.wordList;return Object(l.jsx)("div",{className:"results-list",children:t.map((function(e){return Object(l.jsx)(Q,{data:e},e.word)}))})});n(31);var M=function(){var e=Object(a.useState)([]),t=Object(i.a)(e,2),n=t[0],s=t[1];return Object(l.jsx)("div",{className:"App",children:Object(l.jsxs)("div",{className:"width-container",children:[Object(l.jsx)("p",{className:"app-header",children:"Japanese Vocab Fetcher"}),Object(l.jsx)(g,{setWordList:s}),Object(l.jsx)(K,{wordList:n})]})})},V=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,33)).then((function(t){var n=t.getCLS,a=t.getFID,s=t.getFCP,r=t.getLCP,c=t.getTTFB;n(e),a(e),s(e),r(e),c(e)}))};c.a.render(Object(l.jsx)(s.a.StrictMode,{children:Object(l.jsx)(M,{})}),document.getElementById("root")),V()}],[[32,1,2]]]);
//# sourceMappingURL=main.59d5db71.chunk.js.map