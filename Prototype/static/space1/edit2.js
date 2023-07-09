$(document).ready(function () {
  $("#add-input").click(function () {
    // 수정, 삭제 버튼 비활성화
    const editBtn = document.getElementById("edit-input");
    const deltBtn = document.getElementById("delete-input");
    const reptBtn = document.getElementById("-repair-input");
    const rep2tBtn = document.getElementById("re-repair-input");
    editBtn.classList.add("disabled");
    deltBtn.classList.add("disabled");
    reptBtn.classList.add("disabled");
    rep2tBtn.classList.add("disabled");

    var data = `                <tr>
      <td></td>
      <td>
        <input type="date" class="form-control" name="date_in" id="date_in" value="">
      </td>
      <td>
        <input type="date" class="form-control" name="date_out" id="date_out" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="name" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="point" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="status" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="repair_history" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="cut_area" value="">
      </td>
      <td>
        <input type="text" class="form-control" name="cut_size" value="">
      </td>
    </tr>`;

    $("#input-body").append(data);
  });

  // formStatus 설정해주는 코드들
  $("#edit-input").click(function () {
    var data = `<input type="hidden" name="formStatus" value="1">`;
    $("#input-body").append(data);
  });
  $("#delete-input").click(function () {
    var data = `<input type="hidden" name="formStatus" value="2">`;
    $("#input-body").append(data);
  });
  $("#save-input").click(function () {
    var data = `<input type="hidden" name="formStatus" value="3">`;
    $("#input-body").append(data);
  });
  // repair status Change
  $("#repair-input").click(function () {
    var data = `<input type="hidden" name="formStatus" value="4">`;
    $("#input-body").append(data);
  });
  $("#re-repair-input").click(function () {
    var data = `<input type="hidden" name="formStatus" value="5">`;
    $("#input-body").append(data);
  });
});

// 에러 고쳐야 함 (elementCopy, dateChange)
// {% comment %} <td onclick="elementCopy( '{{ i.date_in }}', 'date_in')"> {% endcomment %}
// {% comment %} <td onclick="elementCopy( '{{ i.date_out }}', 'date_out')"> {% endcomment %}
function elementCopy(a, t) {
  $(`#${t}`).last().val(dateChange(a));
}

function dateChange(a) {
  if (a == "None") {
    return "0";
  }
  var trimmedInput = a.trim(); // 공백 제거

  var dateParts = trimmedInput.split(" "); // 공백으로 분리
  var year = dateParts[0].replace("년", ""); // 연도
  var month = dateParts[1].replace("월", ""); // 월
  var day = dateParts[2].replace("일", ""); // 일

  var formattedDate =
    year + "-" + month.padStart(2, "0") + "-" + day.padStart(2, "0");
  return formattedDate;
}
